import pandas as pd
import glob
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

df_list = []
data_files = glob.glob('backend/data/*.csv')

# Combine all data files, taking email body and label
for data_file in data_files:
    df_temp = pd.read_csv(data_file)

    if 'text_combined' in df_temp.columns:
        df_temp['text'] = df_temp['text_combined']

    elif 'body' in df_temp.columns and 'subject' in df_temp.columns:
        df_temp['text'] = df_temp['subject'].fillna('') + ' ' + df_temp['body'].fillna('')
    
    if 'text' in df_temp.columns and 'label' in df_temp.columns:
        df_temp = df_temp[['text', 'label']]
        df_list.append(df_temp)

# Initialize Data
df = pd.concat(df_list, ignore_index=True)

# Remove new lines, then strip data
df['text'] = df['text'].str.replace(r'[\r\n]+', ' ', regex=True)
df['text'] = df['text'].str.strip()

# Get out train/test data
X = df['text']
Y = df['label']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=27)

# Feature Extraction
tfidf = TfidfVectorizer(ngram_range=(1, 2), stop_words='english', lowercase=True)
X_train_feat = tfidf.fit_transform(X_train)
X_test_feat = tfidf.transform(X_test)

# Model Training
model = LogisticRegression()
model.fit(X_train_feat, Y_train)

# Save our model
with open('backend/model.pkl', 'wb') as file:
    pickle.dump(model, file)

# Save our TF-IDF
with open('backend/tfidf.pkl', 'wb') as file:
    pickle.dump(tfidf, file)