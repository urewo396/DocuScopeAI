from fastapi import FastAPI, File, UploadFile
import io
from PIL import Image
import pytesseract

app = FastAPI()

@app.post("/upload-image/")

async def upload_image(file: UploadFile = File(...)):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes))

    imageContent = pytesseract.image_to_string(image)

    return {"extracted_text": imageContent}