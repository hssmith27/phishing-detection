import kaggle

# Authenticate API
kaggle.api.authenticate()

# Download Phishing Data
kaggle.api.dataset_download_files('naserabdullahalam/phishing-email-dataset', path='backend/data', unzip=True)
