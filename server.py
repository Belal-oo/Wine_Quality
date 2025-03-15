from flask import Flask, request, jsonify
import joblib    
import pandas as pd

with open("wine_quality_model.joblib", "rb") as f:
    model = joblib.load(f)

app = Flask(__name__)


@app.route('/')
def home():
    return "Run Successfully......"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        json_data = request.get_json()
    
        data = pd.DataFrame(json_data)
    
        data.columns = [col.replace("_", " ") for col in data.columns]

    
        expected_columns = ['fixed acidity', 'volatile acidity', 'citric acid', 
                            'residual sugar', 'chlorides', 'free sulfur dioxide', 
                            'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']
        data = data[expected_columns]
    
        # إجراء التنبؤ باستخدام النموذج
        prediction = model.predict(data)
    
        result = "Good Wine" if prediction[0] == 1 else "Bad Wine"
    
        return jsonify({'Prediction': result})
    
    except Exception as e:
        return jsonify({"error": str(e)})



if __name__== '__main__':
    app.run(debug=True)

