# ReqCheck

Hosted on https://req-check.vercel.app/

ReqCheck is a one-click tool designed for UWaterloo students to check their progress toward major requirements. Upload your unofficial transcript or manually enter completed courses, and instantly see which requirements you've met and what’s still pending. You can also simulate how future courses might impact your degree completion with our What-If Analysis feature.

## Tech Stack
- **Frontend:** React, Vite, TailwindCSS, Framer Motion, Particles.js, EmailJS
- **Backend:** FastAPI, pdfplumber
- **Deployment:** Vercel (Frontend), Render (Backend)

<img width="1465" alt="Screen Shot 2025-04-08 at 3 47 02 AM" src="https://github.com/user-attachments/assets/565a86b5-7e69-4f0c-bb54-a7f8ae8860e3" />

We have two folders:

- Backend - With the course_logic directory which contains helper functions in a file, tests in a file, and the check major requirements function for each major that we have in the app. We use a transript parsing script using pdf plumber, We have main.py and saveResults.py which are the FastAPI backend with routes rendered on Render. The dependencies we have are in requirements.txt in case you are curious. 

- Frontend - The frontend follows a standard React structure with folders for pages, components, and routes. It uses the Vite build tool for faster development and includes libraries like Framer Motion, EmailJS, and Particles.js.

## Features
- Upload unofficial transcript or enter courses manually
- Instantly check completed and pending degree requirements
- Perform What-If Analysis to simulate future course completions
- Feedback form with EmailJS integration
- Beautiful UI with Framer Motion animations and particle background


Any questions you have you can mail us at psinghal@uwaterloo.ca and/or r8madan@uwaterloo.ca

Hope you like our project!
