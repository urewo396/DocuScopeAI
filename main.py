from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import io
from PIL import Image
import pytesseract
from transformers import pipeline
from pdf2image import convert_from_path
import tempfile

app = FastAPI()
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

@app.post("/api/document-summary/")
async def image_summary(file: UploadFile = File(...)):
    filename = file.filename.lower()
    if(filename.endswith('png') or filename.endswith('jpg') or filename.endswith('jpeg')):
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes))
        imageContent = pytesseract.image_to_string(image)
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
        summary = summarizer(pagesContent, max_length=150, min_length=40, do_sample=False)
        return {"summary": summary[0]['summary_text']}
    else:
        return {"error": "Unsupported file type"}