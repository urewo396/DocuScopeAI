from fastapi import FastAPI, File, UploadFile, Body, Form
from fastapi.middleware.cors import CORSMiddleware
import io
from PIL import Image
import pytesseract
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from pdf2image import convert_from_path
import tempfile
from utils.clean_text import clean_text
import utils.qwen_qa
import os

app = FastAPI()

#QWEN MODEL INITILIZE
model_id = "Qwen/Qwen1.5-7B-Chat"

tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto",
    torch_dtype="auto",
    trust_remote_code=True
)
llm = pipeline("text-generation", model=model, tokenizer=tokenizer)

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

@app.post("/api/document-summary/")
async def image_summary(file: UploadFile = File(...)):
    filename = file.filename.lower()
    if(filename.endswith('png') or filename.endswith('jpg') or filename.endswith('jpeg')):
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes))
        imageContent = clean_text(pytesseract.image_to_string(image))
        summary = summarizer(imageContent, max_length=150, min_length=40, do_sample=False)
        summary = summary[0]['summary_text']
        return{"summary": summary}
    elif filename.endswith('pdf'):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
            temp_pdf.write(await file.read())
            temp_pdf.flush()
            pages = convert_from_path(temp_pdf.name)
        pagesContent = ""
        for page in pages:
            pagesContent += pytesseract.image_to_string(page)
        
        pagesContent = clean_text(pagesContent)
        summary = summarizer(pagesContent, max_length=150, min_length=40, do_sample=False)
        summary = summary[0]['summary_text']
        os.remove(temp_pdf.name)
        return {"summary": summary}
    else:
        return {"error": "Unsupported file type"}
    

@app.post("/api/raw-text-summary")
async def raw_summary(text: str = Form(...)):
    summary = summarizer(text, max_length=150, min_length=40, do_sample=False)
    summary = summary[0]['summary_text']
    summary = clean_text(summary)
    return {"summary": summary}

@app.post("/api/document-qa")
async def ask_question(question: str = Body(...), file: UploadFile = File(...)):
    filename = file.filename.lower()
    if(filename.endswith('png') or filename.endswith('jpg') or filename.endswith('jpeg')):
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes))
        content = clean_text(pytesseract.image_to_string(image))
    elif filename.endswith('pdf'):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
            temp_pdf.write(await file.read())
            temp_pdf.flush()
            pages = convert_from_path(temp_pdf.name)
        content = ""
        for page in pages:
            content += pytesseract.image_to_string(page)
        
        content = clean_text(content)
        os.remove(temp_pdf.name)
    else:
        return {"error": "Unsupported file type"}
    

    prompt = f"Document:\n{content}\n\nQuestion: {question}\nAnswer:"
    result = llm(prompt, max_new_tokens=200, do_sample=False)[0]['generated_text']
    answer = result.split("Answer:")[-1].strip()
    return {"result": answer}