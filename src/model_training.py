from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import pandas as pd
import joblib

class MuscleGainPredictor:
    def __init__(self):
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)

    def train(self, data, target):
        X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        predictions = self.model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        print(f'Model trained with Mean Squared Error: {mse}')

    def save_model(self, filename):
        joblib.dump(self.model, filename)
        print(f'Model saved to {filename}')

    def load_model(self, filename):
        self.model = joblib.load(filename)
        print(f'Model loaded from {filename}')

    def predict(self, new_data):
        return self.model.predict(new_data)