import os
import cv2
import numpy as np
import tensorflow as tf
import sqlite3
from flask import Flask, render_template, request, jsonify, redirect, url_for
from datetime import datetime

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load trained model
MODEL_PATH = "cotton_disease_model.h5"
model = tf.keras.models.load_model(MODEL_PATH)

# Disease categories
categories = {
    0: "Aphids",
    1: "Army Worm",
    2: "Bacterial Blight",
    3: "Healthy",
    4: "Powdery Mildew",
    5: "Target Spot"
}

# Treatment suggestions
treatment_suggestions = {
    "Target Spot": "Apply Mancozeb (Dithane M-45) or Chlorothalonil (Bravo).",
    "Aphids": "Use insecticides like Imidacloprid (Confidor) or Neem Oil Spray.",
    "Healthy": "No treatment needed. Maintain good agricultural practices.",
    "Powdery Mildew": "Spray Sulfur-based fungicides or Myclobutanil (Systhane).",
    "Bacterial Blight": "Apply Copper Oxychloride (Blitox-50) or Streptocycline.",
    "Army Worm": "Use Bacillus thuringiensis (BT) insecticide or Spinosad."
}

# Database helper functions
def insert_test_result(disease):
    conn = sqlite3.connect("cotton_disease.db")
    cursor = conn.cursor()
    date = datetime.now().strftime("%Y-%m-%d")
    cursor.execute("INSERT INTO test_results (date, disease) VALUES (?, ?)", (date, disease))
    conn.commit()
    conn.close()

def insert_consultancy(name, email, phone, message):
    conn = sqlite3.connect("cotton_disease.db")  # Make sure your DB path is correct
    cursor = conn.cursor()
    
    # Ensure that the 'consultancy_requests' table exists in your database
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS consultancy_requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            phone TEXT,
            message TEXT,
            date TEXT
        )
    """)
    
    cursor.execute("INSERT INTO consultancy_requests (name, email, phone, message, date) VALUES (?, ?, ?, ?, ?)",
                   (name, email, phone, message, datetime.now().strftime("%Y-%m-%d")))
    conn.commit()
    conn.close()


def get_today_test_count():
    conn = sqlite3.connect("cotton_disease.db")
    cursor = conn.cursor()
    date = datetime.now().strftime("%Y-%m-%d")
    cursor.execute("SELECT COUNT(*) FROM test_results WHERE date = ?", (date,))
    count = cursor.fetchone()[0]
    conn.close()
    return count

def get_weekly_tests():
    conn = sqlite3.connect("cotton_disease.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT date, COUNT(*) FROM test_results 
        WHERE date >= DATE('now', '-6 days') 
        GROUP BY date
    """)
    data = cursor.fetchall()
    conn.close()
    return {row[0]: row[1] for row in data}

def get_annual_tests():
    conn = sqlite3.connect("cotton_disease.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT strftime('%m', date) AS month, COUNT(*) FROM test_results
        GROUP BY month
    """)
    data = cursor.fetchall()
    conn.close()
    return {row[0]: row[1] for row in data}

def get_disease_distribution():
    conn = sqlite3.connect("cotton_disease.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT disease, COUNT(*) FROM test_results
        GROUP BY disease
    """)
    data = cursor.fetchall()
    conn.close()
    return {row[0]: row[1] for row in data}

# Routes
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/upload')
def upload():
    return render_template("upload.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route('/consultancy')
def consultancy():
    return render_template("consultancy.html")

@app.route('/dashboard-data')
def dashboard_data():
    # Fetch the counts of tests and diseases from the database
    today_tests = get_today_test_count()
    weekly_tests = get_weekly_tests()
    annual_tests = get_annual_tests()

    # Fetch disease distribution (this example assumes the "test_results" table has the disease names)
    disease_counts = get_disease_distribution()

    return jsonify({
        "today_tests": today_tests,
        "weekly_tests": weekly_tests,
        "annual_tests": annual_tests,
        "disease_counts": disease_counts  # Send real disease data to frontend
    })

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file uploaded", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    # Preprocess image
    img = cv2.imread(file_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (128, 128))
    img = img / 255.0
    img = img.reshape(1, 128, 128, 3)

    prediction = model.predict(img)
    predicted_label = np.argmax(prediction)
    disease_name = categories.get(predicted_label, "Unknown")
    treatment = treatment_suggestions.get(disease_name, "No specific treatment available.")

    # Insert into database
    insert_test_result(disease_name)

    return render_template("result.html", image=file_path, disease=disease_name, treatment=treatment)

@app.route('/submit-consultancy', methods=['POST'])
def submit_consultancy():
    # Retrieve the data from the form
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']

    # Insert the data into the database
    insert_consultancy(name, email, phone, message)

    # After submission, redirect back to the consultancy page or a success page
    return redirect(url_for('consultancy'))


if __name__ == "__main__":
    app.run(debug=True)
