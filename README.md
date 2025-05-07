Here is your revised and properly punctuated project documentation:

---

# Cotton Disease Detection

🌿 **Cotton Disease Detection System** (with Dashboard & Consultancy Portal)

A professional web-based system built with Flask that uses a deep learning model to detect cotton plant diseases from uploaded images. The platform features real-time reporting, dashboards, and a user-friendly consultancy form backed by a database and Google Form integration.

---

## 📁 Project Directory Structure

```
cotton-disease-detection/
│
├── app.py                  # Main Flask backend app
├── database.py             # Optional: DB schema creator (one-time run)
├── cotton_disease.db       # SQLite DB (auto-generated after prediction/consultancy)
├── cotton_disease_model.h5 # Pre-trained CNN model
│
├── static/
│   ├── css/
│   │   └── style.css       # Main stylesheet (theme)
│   └── uploads/            # Uploaded images saved here
│
├── templates/
│   ├── index.html          # Home page
│   ├── upload.html         # Image upload & prediction
│   ├── dashboard.html      # Real-time charts and analytics
│   ├── consultancy.html    # Consultancy booking form + Google Form link
│   └── result.html         # Prediction result view (internal CSS)
│
└── README.md               # You're here!
```

---

## 💡 Features

* Upload images of cotton leaves to predict diseases.
* Displays treatment suggestions for detected diseases.
* Stores test results in SQLite database.
* Dynamic dashboard showing:

  * Today's test count
  * Weekly test trends
  * Annual test summary
  * Disease distribution pie chart
* Professional **consultancy form**:

  * Saves details to the database
  * Directs users to an additional Google Form
* Fully responsive and visually appealing front-end design

---

## ⚙️ Technologies Used

* Python 3.10+
* Flask
* TensorFlow / Keras
* OpenCV
* SQLite3
* HTML, CSS (custom themed)
* Chart.js for dashboard charts

---

## 📥 Download the Pre-trained CNN Model

Download it from here:
[https://drive.google.com/file/d/1aDkw8vqbUbbuWGQb8K9PNrQ5MbXTDNDr/view?usp=drive\_link](https://drive.google.com/file/d/1aDkw8vqbUbbuWGQb8K9PNrQ5MbXTDNDr/view?usp=drive_link)

---

## 📊 Dashboard

`/dashboard` — Visualize trends from real test data.

All charts update automatically from `cotton_disease.db`.

---

## 📝 Consultancy Booking

`/consultancy` — Submit name, email, phone, and message.

Data is stored in the `consultancy_requests` table in the database.

A Google Form link opens in a new tab for additional information.

---

## 📌 Notes

* Make sure `cotton_disease_model.h5` exists in the root directory.
* `cotton_disease.db` will be created automatically after the first prediction or consultancy form submission.
* You can run `database.py` manually once to pre-create the schema if needed.
* All uploaded files are saved in `static/uploads/`.

---

## 🙌 Credits

Developed as part of a final-year project in Computer Science & Engineering
**By:** Vinod Kumar M. M., Kerthi Vaasan R. S., Sanoop N.
**Institution:** Er. Perumal Manimekalai College of Engineering, 2025

---

Would you like this formatted into a PDF or added to your GitHub README?
