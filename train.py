import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Initialize Dataframe
df = pd.read_csv('data/CEAS_08.csv')

# Drop unneeded columns
df = df.drop(columns=['receiver', 'date'])

# Replace null values with empty string
df['body'] = df['body'].fillna('')

# Remove punctuation and new lines, then strip data
df['body'] = df['body'].str.replace(r'[^\w\s]', '', regex=True)
df['body'] = df['body'].str.replace(r'[\r\n]+', ' ', regex=True)
df['body'] = df['body'].str.strip()

# Get out train/test data
X = df['body']
Y = df['label']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=27)

# Feature Extraction
tfidf = TfidfVectorizer(min_df=1, stop_words='english', lowercase=True)
X_train_feat = tfidf.fit_transform(X_train)
X_test_feat = tfidf.transform(X_test)

# Model Training
model = LogisticRegression()
model.fit(X_train_feat, Y_train)

# Test accuracy of model
Y_pred = model.predict(X_test_feat)
print(accuracy_score(Y_test, Y_pred))
