# ⚖️ Legal Analyzer

An AI-powered Legal Document Analyzer that helps users upload legal documents, extract key information, identify important clauses, summarize content, and provide AI-assisted insights for easier understanding of complex legal agreements.

---

## 🚀 Features

- 📄 Upload legal documents (PDF/DOCX)
- 🤖 AI-powered legal document analysis
- 📝 Automatic summary generation
- 🔍 Clause extraction
- ⚠️ Risk identification
- 📋 Key obligations and responsibilities detection
- 💬 AI chatbot for legal document queries
- 📊 Clean and interactive dashboard
- 📁 Secure document management

---

## 🏗️ System Architecture

```
                User
                  │
                  ▼
          React Frontend
                  │
          REST API Requests
                  │
                  ▼
        Spring Boot Backend
                  │
      ┌───────────┴───────────┐
      │                       │
      ▼                       ▼
 AI Service (LLM)         Database
      │                       │
      └───────────┬───────────┘
                  ▼
          Analysis Result
                  │
                  ▼
            User Interface
```

---

# 🛠 Tech Stack

### Frontend

- React.js
- Tailwind CSS
- Axios
- React Router

### Backend

- Java
- Spring Boot
- Spring Security
- Spring Data JPA

### Database

- MongoDB / MySQL

### AI

- OpenAI / Groq API
- LangChain (if used)

### File Storage

- Local Storage / Cloudinary

---

# 📂 Project Structure

```
legal-analyzer
│
├── frontend
│   ├── src
│   ├── components
│   ├── pages
│   └── services
│
├── backend
│   ├── controller
│   ├── service
│   ├── repository
│   ├── model
│   ├── config
│   └── util
│
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/Akshaysolan/legal-analyzer.git

cd legal-analyzer
```

---

## Backend

```bash
cd backend

mvn clean install

mvn spring-boot:run
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

---

# 📸 Screenshots

## Home

_Add Screenshot_

## Document Upload

_Add Screenshot_

## AI Analysis

_Add Screenshot_

## Dashboard

_Add Screenshot_

---

# 🔍 Workflow

1. Upload Legal Document
2. Backend validates file
3. Document text is extracted
4. AI model analyzes content
5. Important clauses are identified
6. Risks are highlighted
7. Summary is generated
8. Results are displayed to the user

---

# 📈 Future Enhancements

- OCR support
- Multi-language legal documents
- AI-powered contract comparison
- Digital signature verification
- Clause recommendation system
- Export analysis as PDF
- Team collaboration

---

# 👨‍💻 Author

**Akshay Solanke**

- GitHub: https://github.com/Akshaysolan
- LinkedIn: *(Add your LinkedIn URL)*

---

# ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub.

---

# 📄 License

This project is licensed under the MIT License.
