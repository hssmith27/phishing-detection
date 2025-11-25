import pickle

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Read in model
with open('backend/model.pkl', 'rb') as file:
    model = pickle.load(file)

# Read in TF-IDF
with open('backend/tfidf.pkl', 'rb') as file:
    tfidf = pickle.load(file)

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    subject = data.get('subject', '')
    body = data.get('body', '')
    feat = tfidf.transform([subject +  " " + body])
    return jsonify({"probability": round(model.predict_proba(feat)[0][1], 3)})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)