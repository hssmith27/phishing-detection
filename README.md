# Phishing Classification
This project trains a model using TF-IDF and Logistic Regression to classify emails as phishing or not.  
It includes a front end where users can submit email content and receive the probability that the email is a phishing attempt.

## How It's Made:

**Front End:** React & Typescript
**Back End:** Python & Flask

## How to Use:

1. Download Kaggle data by running `download_data.py`
**NOTE:** Running `download_data.py` requires a Kaggle API key to authenticate.
2. Train the model by running `train.py`
3. Start the backend by running `predictor.py`
4. Start the frontend by entering the frontend directory and running `npm start` in a new terminal
5. Enter in the subject and body of an email and get the probability of it being a phishing attempt!

## Credits:
- *Al-Subaiey, A., Al-Thani, M., Alam, N. A., Antora, K. F., Khandakar, A., & Zaman, S. A. U. (2024, May 19) Novel Interpretable and Robust Web-based AI Platform for Phishing Email Detection. ArXiv.org. https://arxiv.org/abs/2405.11619*