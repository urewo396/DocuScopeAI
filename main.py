from fastapi import FastAPI, File, UploadFile, Body, Form
from fastapi.middleware.cors import CORSMiddleware
import io
from PIL import Image
import pytesseract
from transformers import pipeline
from pdf2image import convert_from_path
import tempfile
from utils.clean_text import clean_text
import os
import requests

app = FastAPI()
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

#headers for OpenRouter API
headers = {
  "Authorization": "Bearer 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",
  "Content-Type": "application/json"
}


#route that summarizes an image passed, gives away summary and content of an image (as a string)
@app.post("/api/document-summary/")
async def image_summary(file: UploadFile = File(...)):
    filename = file.filename.lower()
    if(filename.endswith('png') or filename.endswith('jpg') or filename.endswith('jpeg')):
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes))
        imageContent = clean_text(pytesseract.image_to_string(image))
        summary = summarizer(imageContent, max_length=150, min_length=40, do_sample=False)
        summary = summary[0]['summary_text']
        return{"summary": summary,
               "content": imageContent}
    elif filename.endswith('pdf'):
        temp_pdf_name = None
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
                temp_pdf.write(await file.read())
                temp_pdf.flush()
                temp_pdf_name = temp_pdf.name
                pages = convert_from_path(temp_pdf_name)
            pagesContent = ""
            for page in pages:
                pagesContent += pytesseract.image_to_string(page)
            pagesContent = clean_text(pagesContent)
            summary = summarizer(pagesContent, max_length=150, min_length=40, do_sample=False)
            summary = summary[0]['summary_text']
            return {"summary": summary, "content": pagesContent}
        finally:
            if temp_pdf_name and os.path.exists(temp_pdf_name):
                os.remove(temp_pdf_name)
    else:
        return {"error": "Unsupported file type"}
    

#This route is used for summarizing raw text (string) e.g. you have a NDA as a string and want to summarize it, then
#you can pass it to this route
@app.post("/api/raw-text-summary/")
async def raw_summary(text: str = Form(...)):
    summary = summarizer(text, max_length=150, min_length=40, do_sample=False)
    summary = summary[0]['summary_text']
    summary = clean_text(summary)
    return {"summary": summary}

#this route is for asking questions about a document, you have to pass an image or a pdf and ask a (string) question
#and Lawyer AI is going to answer your questions
@app.post("/api/document-qa/")
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
    

    data = {
        "model": "meta-llama/llama-3.3-8b-instruct:free",
        "messages": [
            {"role": "system", "content": "You are an AI lawyer that needs to help users."},
            {"role": "user", "content": "this is a document: " + content + "\n Question: " + question}
        ]
    }
    r = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
    return{"response": (r.json()['choices'][0]['message']['content'])}
