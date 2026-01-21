📸 AI Smart Gallery



AI Smart Gallery is a full-stack AI-powered photo management system that automatically organizes images by people, events, and moments using face recognition — similar to Google Photos, but fully self-hosted.



🚀 Key Features



🧠 AI Face Recognition

Automatically detects and groups faces across thousands of photos using InsightFace.



🔍 Visual Search

Upload a face image to instantly find all matching photos.



📅 Smart Event Detection

Groups photos into events based on timestamps (e.g. trips, weddings, parties).



✨ AI-Smart Collages

Generates collages with intelligent face-aware cropping.



🎨 Modern UI

Animated, glassmorphism-style interface with interactive previews.



🔐 Authentication System

Secure user login \& registration.



🛠 Tech Stack

Backend



Django 5



PostgreSQL



Gunicorn (production-ready)



AI / Machine Learning



InsightFace



ONNX Runtime



OpenCV



Scikit-learn



Frontend



HTML5



CSS3 (Glassmorphism, animations)



🧠 AI Workflow



Face Detection → Extracts faces from uploaded images



Embedding Generation → Converts faces into vectors



Clustering (DBSCAN) → Groups the same person across photos



Event Grouping → Detects events using time gaps



Search \& Retrieval → Matches faces using cosine similarity



⚙️ Local Setup

1️⃣ Clone the repository

git clone https://github.com/bytebyshreya/ai-smart-gallery.git

cd ai-smart-gallery



2️⃣ Create virtual environment

python -m venv venv

venv\\Scripts\\activate



3️⃣ Install dependencies

pip install -r requirements.txt



4️⃣ Run migrations

cd core

python manage.py migrate



5️⃣ Start development server

python manage.py runserver





Visit:

👉 http://127.0.0.1:8000/



🗄 Database



PostgreSQL



Django ORM for schema management



Ready for cloud databases (RDS / managed PostgreSQL)



👩‍💻 Author



Shreya Ghosh

GitHub: @bytebyshreya



⭐ Why this project matters



This project demonstrates:



Real-world AI integration



Backend + ML system design



Production-ready Django architecture



Clean Git \& dependency management

