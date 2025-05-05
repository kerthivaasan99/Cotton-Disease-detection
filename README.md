# Cotton-Disease-detection
# 🌿 Cotton Disease Detection System (with Dashboard & Consultancy Portal)

A professional web-based system built with Flask that uses a deep learning model to detect cotton plant diseases from uploaded images. The platform features real-time reporting, dashboards, and a user-friendly consultancy form backed by a database and Google Form integration.

---

## 📁 Project Directory Structure

cotton-disease-detection/

│

├── app.py # Main Flask backend app

├── database.py # Optional: DB schema creator (one-time run)

├── cotton_disease.db # SQLite DB (auto-generated after prediction/consultancy)

├── cotton_disease_model.h5 # Pre-trained CNN model

│
├── static/

│ ├── css/

│ │ └── style.css # Main stylesheet (theme)

│ └── uploads/ # Uploaded images saved here

│

├── templates/

│ ├── index.html # Home page

│ ├── upload.html # Image upload & prediction

│ ├── dashboard.html # Real-time charts and analytics

│ ├── consultancy.html # Consultancy booking form + Google Form link

│ └── result.html # Prediction result view (internal CSS)

│

└── README.md # You're here!

yaml
Copy
Edit

---

## 💡 Features

- Upload images of cotton leaves to predict disease.
- Displays treatment suggestions for detected disease.
- Stores test results in SQLite database.
- Dynamic dashboard showing:
  - Today's test count
  - Weekly test trends
  - Annual test summary
  - Disease distribution pie chart
- Professional **consultancy form**:
  - Saves details to DB
  - Directs users to additional Google Form
- Fully responsive & visually appealing front-end design

---

## ⚙️ Technologies Used

- Python 3.10+
- Flask
- TensorFlow / Keras
- OpenCV
- SQLite3
- HTML, CSS (custom themed)
- Chart.js for dashboard charts

---

# Download the Pre-trained CNN model
form here : https://drive.google.com/file/d/1aDkw8vqbUbbuWGQb8K9PNrQ5MbXTDNDr/view?usp=drive_link
