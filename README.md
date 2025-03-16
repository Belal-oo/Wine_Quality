# Wine Quality Prediction

## Overview
This project is a **Flask API** that predicts wine quality based on various chemical properties. The model is trained using machine learning techniques and deployed on an **AWS EC2 instance**.

## Features
- 🏗 **Flask-based API** for predicting wine quality.
- 🧠 **Machine Learning Model** trained on the Wine Quality dataset.
- 🚀 **Deployment on AWS EC2** for continuous availability.
- 📊 **Logging & Debugging** to track API performance.

## Installation & Setup
### Prerequisites
- Python 3.x
- Flask
- Virtual Environment (`venv`)

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Belal-oo/Wine_Quality.git
cd Wine_Quality
```

### 2️⃣ Set up a virtual environment
```bash
python3 -m venv ec2_env
source ec2_env/bin/activate  # On Windows use: ec2_env\Scripts\activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

## Running the API
### Locally
```bash
python server.py
```
API will be available at: `http://127.0.0.1:8888`

### On AWS EC2
```bash
nohup python server.py > output.log 2>&1 &
```
The API will run in the background, accessible via:
👉 **[Live Model](http://ec2-51-20-71-235.eu-north-1.compute.amazonaws.com:8888/)**

## API Endpoints
| Method | Endpoint       | Description                     |
|--------|---------------|---------------------------------|
| POST   | `/predict`    | Predict wine quality based on input features |

### Example Request
```bash
curl -X POST "http://ec2-51-20-71-235.eu-north-1.compute.amazonaws.com:8888/predict" -H "Content-Type: application/json" -d '{"features": [7.4, 0.7, 0.0, 1.9, 0.076, 11.0, 34.0, 0.9978, 3.51, 0.56, 9.4]}'
```

## Deployment on AWS EC2
To keep the server running permanently:
1. Use `tmux` or `screen` to run the server.
2. Set up `systemd` to restart the API after reboot.

## Author
👤 **Belal-oo**  
📌 GitHub: [Belal-oo](https://github.com/Belal-oo)

---
✨ *Feel free to contribute or report any issues!* ✨

