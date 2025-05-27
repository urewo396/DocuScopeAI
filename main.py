from fastapi import FastAPI, File, UploadFile
import io
from PIL import Image
import pytesseract
from transformers import pipeline

app = FastAPI()
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

@app.post("/document-summary/")
async def image_summary(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes))
    imageContent = pytesseract.image_to_string(image)
    summary = summarizer(imageContent, max_length=150, min_length=40, do_sample=False)
    summary = summary[0]['summary_text']
    return{"summary": summary}