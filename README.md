# 🎓 ReqCheck – Degree Progress Checker for UWaterloo Students

[Live Demo →] (https://req-check.vercel.app/) &nbsp;&nbsp;&nbsp;•&nbsp;&nbsp;&nbsp;[Frontend Repo](https://github.com/priyanshusinghal12/ReqCheck/tree/main/frontend) &nbsp;&nbsp;&nbsp;•&nbsp;&nbsp;&nbsp;[Backend Repo](https://github.com/priyanshusinghal12/ReqCheck/tree/main/backend)

**ReqCheck** is a web-based academic audit platform built to help University of Waterloo students track and plan their progress toward graduation. Upload your unofficial transcript or manually enter completed courses, select your major, and instantly see which requirements you’ve completed — and what’s still pending. Then simulate future semesters with What-If Analysis, and even save your progress for later.

---

## 🚀 Demo Walkthrough

### 🔥 Clean, Responsive Landing Page

> ![Landing Page – Desktop](https://github.com/user-attachments/assets/1337bc6d-9fb2-43fb-816d-c68b9c95a86d)

---

### 📥 Upload Transcript or Enter Manually

Choose your major and either upload your unofficial transcript (we’ll parse it for you), or enter your completed courses manually.

---

### ✅ Real-Time Degree Progress Checklist

> ![Results Page - Initial](https://github.com/user-attachments/assets/7542b090-222e-4aa4-a456-f2243433f796)

Instantly shows which degree requirements are complete and what remains.

---

### 🧪 What-If Analysis

> ![What-If Analysis with Highlighted Tags](https://github.com/user-attachments/assets/8e123f0b-2c3f-40ac-9ea3-967366402189)

Try out hypothetical course selections to simulate how future terms will impact your graduation plan — fulfilled requirements update in real-time.

---

### 💾 Login + Saved Results Dashboard

> ![Saved Results Page](https://github.com/user-attachments/assets/90daf106-843c-4775-b295-9931a3e24414)

Log in with Google and save your progress. Revisit your results later without needing to re-upload anything.

---

### 💬 Anonymous Feedback Form

> ![Feedback Form](https://github.com/user-attachments/assets/1b1de6f4-1d73-4ac3-a794-bfe37555f4b8)

Let us know what you think with a star rating and message, sent directly to our inbox using EmailJS.

---

## 🧠 Tech Stack

### Frontend
- **React** + **Vite**
- **Tailwind CSS** for fast, responsive styling
- **Framer Motion** for smooth UI animations
- **Particles.js** for interactive hero effects
- **EmailJS** for submitting feedback

### Backend
- **FastAPI** for REST API endpoints
- **pdfplumber** for parsing PDF transcripts
- **Custom logic** for per-major degree evaluation
- Deployed via **Render**

### Auth & Deployment
- **Firebase Auth** (Google sign-in)
- **Vercel** (Frontend deployment)
- **Render** (Backend deployment)

---

## 🧩 Features

| Feature                         | Description                                                                 |
|----------------------------------|-----------------------------------------------------------------------------|
| 📄 Transcript Parsing            | Upload unofficial transcripts in PDF format, parsed via `pdfplumber`.       |
| ⌨️ Manual Course Entry           | Input course codes yourself — no file upload required.                      |
| 📊 Real-Time Requirement Audit   | Instantly view fulfilled vs pending requirements for your selected major.   |
| 🧪 What-If Simulation            | Check how planned future courses impact your graduation progress.           |
| 🔐 Secure Login                  | Firebase authentication (Google) to safely save and revisit results.        |
| 💾 Save & Retrieve Results       | View your past uploads and analyses anytime after logging in.               |
| 💬 Feedback Collection           | Submit a star rating and feedback message using EmailJS.                    |
| 🌑 Dark Mode UI                  | Sleek, accessible dark theme with gold accents.                             |
| 📱 Fully Responsive              | Optimized layout and UX for phones, tablets, and desktops.                  |
| 🧠 Clean Architecture            | Modular code with clear separation of frontend/backend logic.               |
| 🎨 Animations & Effects         | Framer Motion transitions and Particles.js for a modern feel.               |
| 📤 Future-Ready Structure        | Easy to expand with more majors, schools, or export/share features.         |

---

## 📁 Folder Structure

```bash
ReqCheck/
├── frontend/          # React + Vite frontend
│   ├── components/
│   ├── pages/
│   └── routes/
├── backend/           # FastAPI backend logic
│   ├── course_logic/  # Requirement-checking logic
│   ├── main.py        # API endpoints
│   └── saveResults.py # Save/load results by user
