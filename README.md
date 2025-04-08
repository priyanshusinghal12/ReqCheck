# ReqCheck

Hosted on https://req-check.vercel.app/

ReqCheck is a one-click tool designed for UWaterloo students to check their progress toward major requirements. Upload your unofficial transcript or manually enter completed courses, and instantly see which requirements you've met and what’s still pending. You can also simulate how future courses might impact your degree completion with our What-If Analysis feature.

We have two folders:

- Backend - with the course_logic directory which contains helper functions in a file, tests in a file, and the check major requirements function for each major that we have in the app. We use a transript parsing script using pdf plumber, We have main.py and saveResults.py which are the FAST API backend with routes rendered on Render. The dependencies we have are in requirements.txt in case you are curious. 

- Frontend - we have folders with pages, components and routes. A basic React structure using the Vite Framework. We are using a lot of libraries like Framer Motion, EmailJS, ParticlesJS etc. Dependencies are in package*.json files in case you are curious. 

Any questions you have you can mail us at psinghal@uwaterloo.ca and/or r8madan@uwaterloo.ca


Hope you like our project!
