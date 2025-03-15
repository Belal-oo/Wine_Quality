from flask import Flask, request, jsonify ,render_template
import joblib    
import pandas as pd
import numpy as np 

app = Flask(__name__)

with open("wine_quality_model.joblib", "rb") as f:
    model = joblib.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        int_features = [float(x) for x in request.form.values()]

        final_features = [np.array(int_features)]
        
        data = pd.DataFrame(final_features)
    
    
        expected_columns = ['fixed acidity', 'volatile acidity', 'citric acid', 
                            'residual sugar', 'chlorides', 'free sulfur dioxide', 
                            'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']
        
        
        if len(data.columns) == len(expected_columns):
            data.columns = expected_columns
        else:
            raise ValueError("Number of input features does not match expected features.")
        
        
        prediction = model.predict(data)
    
        result = "Good Wine" if prediction[0] == 1 else "Bad Wine"
    
        return render_template('index.html', prediction_text='Prediction {}'.format(result))
    except Exception as e:
        app.logger.error(f"Error during prediction: {str(e)}")
        return render_template('index.html', prediction_text='Prediction: {}'.format(result))

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True,port=8888)
