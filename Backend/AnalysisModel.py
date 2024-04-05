import numpy as np;
import pandas as pd;

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

dataset = pd.read_csv('./Leetcode.csv')

X = dataset.drop(['username','OurRating'],axis=1)
y = dataset.iloc[:,-1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)




def PredictRating(data):
    rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)

    # Train the model
    
    rf_regressor.fit(X_train, y_train)
    data = pd.DataFrame([data], index=['0'])
    # print(data)
    return rf_regressor.predict(data)




