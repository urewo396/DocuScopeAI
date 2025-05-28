# 📄 DocuScopeAI

**DocuScopeAI** is an AI-powered document assistant that lets you upload images or PDFs and get instant text extraction, summarization, and question answering, all via an easy FastAPI backend. It's designed to be extendable with features like audio transcription, search, user dashboards, and more!

---

## 🚀 Features (Implemented)

- **File Upload API:** Upload images (JPG, PNG) or PDFs for processing
- **OCR Extraction:** Uses Tesseract OCR to extract text from images and PDFs
- **Text Summarization:** Summarizes extracted text using Hugging Face transformers (BART model)
- **Document Q&A:** Ask questions about any uploaded document (leverages LLMs for natural language answers)
- **Clean Text Utility:** Cleans and prepares extracted text for further processing
- **Async FastAPI Endpoints:** Modern Python API framework

---

## 🛣️ Roadmap

### AI Document Assistant – 10-Week Roadmap 🧠

- **Setup & Core Skills**
  - FastAPI backend, file upload, Hugging Face models, OCR pipeline
- **Frontend Basics**
  - Next.js app, file upload UI, show extracted text, basic routing
- **Backend Expansion**
  - Async task processing, database integration, file/result history
- **Search & Elastic Magic**
  - Full-text search, frontend search bar, filters, highlights
- **Auth + User Dashboard**
  - User authentication, personal dashboards, doc sharing
- **AI Features**
  - Visual Q&A, scanned forms, auto-insights, voice input (optional)
- **Performance + UI Polish**
  - Upload progress, mobile support, analytics, security, docs
- **Deploy & Portfolio Polish**
  - Cloud deployment, killer README, demo video, blog post

**Bonus Ideas**
- PDF annotations w/ highlights
- Slack/Gmail integrations
- Stripe: Monetize with Pro features

---

## ✅ What's Included

- Backend code for document OCR, summarization, and Q&A (Python, FastAPI)
- Tesseract OCR + Hugging Face summarization pipeline
- Endpoints:
  - `POST /api/document-summary/` — Summarize an image or PDF
  - `POST /api/raw-text-summary/` — Summarize raw text
  - `POST /api/document-qa/` — Q&A about an uploaded document

## 🚧 What's NOT Included (Yet)

- Frontend (React/Next.js UI)
- User authentication & dashboards
- Database for persistent storage/history
- Full-text search
- Cloud deployment scripts
- Advanced AI features (voice, auto-insights, etc.)
- Monetization/integrations

---

## 🛠️ Getting Started

1. **Clone the repo:**
   ```bash
   git clone https://github.com/urewo396/DocuScopeAI.git
   cd DocuScopeAI
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Tesseract OCR:**  
   - Windows: Download from [here](https://github.com/tesseract-ocr/tesseract)
   - Linux: `sudo apt install tesseract-ocr`
   - Mac: `brew install tesseract`

4. **Set up environment variables:**  
   (Recommended: do **not** hardcode API keys. Use `.env` or your OS environment.)

5. **Run the API:**
   ```bash
   uvicorn main:app --reload
   ```

## 📦 API Usage

### Summarize a Document
`POST /api/document-summary/`  
Upload a file (`image` or `pdf`).  
Returns a summary and the extracted content.

### Summarize Raw Text
`POST /api/raw-text-summary/`  
Send a string (`text`).  
Returns a summary.

### Document Q&A
`POST /api/document-qa/`  
Upload a file + send a question (`question`).  
Returns an AI-generated answer.

---

## 🤝 Contributing

PRs welcome! Check the roadmap, open an issue, or suggest a feature.

---

## 📅 Project Status

- Core backend features: **done**
- Frontend, auth, search, and advanced features: **coming soon!**

---

## 📝 License

Add your license here (MIT, Apache 2.0, etc.)

---

## 🌐 Links

- GitHub: [urewo396/DocuScopeAI](https://github.com/urewo396/DocuScopeAI)
