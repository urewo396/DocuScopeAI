# DocuScopeAI

> AI-powered document understanding web app that scans real-world business docs (NDAs, contracts, invoices, T&Cs) to extract key clauses, summarize, flag risks, and suggest legal edits. Helping SMBs and freelancers get legal clarity without hiring a lawyer.

---

## 🚀 Features

- **OCR & Text Extraction:** Extract text from uploaded documents using Hugging Face OCR models.
- **Clause Summarization:** Summarizes key clauses for quick reading.
- **Risk & Compliance Flags:** Detects risky or non-compliant terms automatically.
- **Legal Edit Suggestions:** Suggests how to improve or fix legal language.
- **Document Indexing & Search:** Stores docs with fast search & versioning support.
- **Real-time Processing:** Upload and get instant insights on your docs.
- **Version Tracking:** Keep track of document changes over time.
- **Clause Generation:** (Planned) Generate custom clauses based on user needs.

---

## 🛠️ Tech Stack

- Backend: FastAPI (or Node.js, your pick)
- AI Models: Hugging Face Transformers for OCR, summarization, and Q&A
- Database: PostgreSQL for storing docs & metadata
- Cache: Redis for speedy processing & caching
- Frontend: React + Tailwind CSS + Next.js
- Hosting: Vercel (frontend), Railway / Fly.io (backend)
- Others: Real-time WebSockets for live doc processing

---

## 📦 Getting Started

### Prerequisites

- Node.js & npm/yarn
- Python 3.9+
- PostgreSQL
- Redis
- Hugging Face API token (optional, if using hosted models)

### Installation

1. Clone the repo  
```bash
git clone https://github.com/yourusername/DocuScopeAI.git
cd DocuScopeAI
```
2. Setup backend environment
```bash
cd backend
pip install -r requirements.txt
```
3. Setup frontend environment
```bash
cd ../frontend
npm install
```
4. Configure .env files for backend & frontend with your DB creds, API keys, etc.

## 🚀 Running Locally
- Make sure PostgreSQL & Redis servers are running
-Run backend
```bash
uvicorn main:app --reload
```
- Run frontend
```bash
npm run dev
```

## 🤖 How it Works
1. Upload your document (PDF, DOCX, etc).
2. Backend extracts text using OCR + AI models.
3. Key clauses get summarized & flagged for risks.
4. Suggestions pop up for legal edits and improvements.
5. Documents get indexed & stored for quick search and version control.
6. Users can track changes and access document history.
7. (Future) Generate custom clauses based on user input.

## 🧑‍💻 Usage
- Drag & drop or upload business documents.
- Review AI-generated summaries and flagged risks.
- Accept or reject suggested edits.
- Search your document archive with keywords or clauses.
- Track document versions and history for compliance.
