from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score


data = pd.read_csv('./RawData/training_data_final.csv', usecols=[1, 2], header=0)

X_train, X_test, Y_train, Y_test = train_test_split(data['tweet'], data['sentiment'], test_size=0.1, random_state=1)


vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)
print(X_train)

naive_bayes = MultinomialNB()
naive_bayes.fit(X_train_vectorized, Y_train)
prediction = naive_bayes.predict(X_test_vectorized)

print('Accuracy score: ', accuracy_score(Y_test, prediction))
