# 📄 DocuScopeAI

> AI-powered document summarizer — helping SMBs and freelancers understand legal docs without a lawyer.

DocuScopeAI is your future go-to web app for scanning and understanding business documents like NDAs, contracts, invoices, and T&Cs. Right now? We're keeping it lean — you give us text, and we summarize it. But big things are coming 👀

---

## ✅ Current Features (MVP v0.1)

- **🧠 Text Summarization Route**  
  Send text to `/summarize`, and get a clean, AI-generated summary. Powered by Hugging Face Transformers.

```bash
POST /summarize
Content-Type: application/json

{
  "text": "Your long document text here..."
}
```

Response:
```json
{
  "summary": "Short summary here..."
}
```

---

## 🛠️ Tech Stack

- Backend: FastAPI (Python)
- AI: Hugging Face Transformers (summarization model)
- Hosting: Railway / Fly.io (soon™)

---

## 🧪 Running Locally

1. Clone the repo  
```bash
git clone https://github.com/yourusername/DocuScopeAI.git
cd DocuScopeAI
```

2. Install dependencies  
```bash
pip install -r requirements.txt
```

3. Run the server  
```bash
uvicorn main:app --reload
```

4. Test the route with Postman, curl, or a frontend later on.

---

## 🌱 Planned Features

This project’s just sprouting — here’s what’s coming:

- **🖼️ OCR & File Uploads**  
  Upload PDFs, DOCXs, and images — we’ll extract the text for you.

- **📌 Clause Detection**  
  Auto-extract key clauses like payment terms, liability, NDA scope, etc.

- **🚨 Risk & Compliance Alerts**  
  Spot sketchy or non-compliant clauses with red flag alerts.

- **✍️ Smart Edit Suggestions**  
  Suggest edits to improve clarity, reduce risk, or meet compliance.

- **🔎 Document Search & Indexing**  
  Store uploaded docs and search by keyword or clause type.

- **📜 Version Tracking**  
  Compare document versions and track changes over time.

- **⚙️ Clause Generator (AI)**  
  Generate custom clauses based on what you need.

---

## 🧠 Why It Matters

Legal docs are hell to read. DocuScopeAI will make them simple, safe, and understandable — without paying for a lawyer every time.

## 👀 Stay Tuned

Follow the repo to watch this evolve into a full AI doc assistant. PRs and ideas welcome!
