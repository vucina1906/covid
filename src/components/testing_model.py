import pickle
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd

with open('artifacts/preprocessor.pkl','rb') as file:
    preprocessor = pickle.load(file)

with open('artifacts/model.pkl','rb') as file:
    model = pickle.load(file)

df = pd.read_csv("artifacts/test.csv")
X_test = df.drop("DIED",axis=1)
X_test = preprocessor.fit_transform(X_test)
y_test = df["DIED"]
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test,predictions)*100
print(f'Accuracy: {accuracy:.2f} %')
