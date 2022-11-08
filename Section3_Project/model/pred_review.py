import pandas as pd
from category_encoders import OneHotEncoder
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv("/Users/hamhwijin/Section3_Project/selenium/review_modify.csv")

X = df.drop(['score','name'], axis=1)
y = df["score"]

encoder = OneHotEncoder(cols=['tags','like'], use_cat_names=True)
X_ohe = encoder.fit_transform(X)

model = LinearRegression()
model.fit(X_ohe, y)


with open('encoder.pkl', 'wb') as pickle_encoder:
    pickle.dump(encoder, pickle_encoder)

with open('model.pkl', 'wb') as pickle_model:
    pickle.dump(model, pickle_model)