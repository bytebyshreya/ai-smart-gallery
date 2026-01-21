📸 AI Smart Gallery

AI Smart Gallery is a full-stack AI-powered photo management system that automatically organizes images by people, events, and moments using face recognition — inspired by Google Photos.

🚀 Features

🧠 Face Recognition – Detects and groups people across photos using InsightFace

🔍 Visual Search – Find photos by uploading a face image

📅 Smart Events – Automatically groups photos into events

✨ AI Collages – Face-aware intelligent image cropping

🔐 Authentication – Secure login & user accounts

🎨 Modern UI – Animated, glassmorphism-based interface

🛠 Tech Stack

Backend: Django 5, PostgreSQL
AI / ML: InsightFace, ONNX Runtime, OpenCV, Scikit-learn 
Frontend: HTML

⚙️ Local Setup
git clone https://github.com/bytebyshreya/ai-smart-gallery.git
cd ai-smart-gallery
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
cd core
python manage.py migrate
python manage.py runserver


Access: http://127.0.0.1:8000/

☁️ Deployment Ready

PostgreSQL supported

Cloud-ready (AWS / Docker / S3 integration planned)

GitHub-managed codebase

👩‍💻 Author

Shreya Ghosh
GitHub: @bytebyshreya
