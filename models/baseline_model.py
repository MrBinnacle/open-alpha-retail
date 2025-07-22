import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os

class BaselineETHModel:
    def __init__(self):
        self.model = LinearRegression()

    def load_data(self, csv_path):
        df = pd.read_csv(csv_path)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df = df.set_index('timestamp').sort_index()
        df = df[['ETH_price', 'stETH_supply']].dropna()
        return df

    def train(self, df):
        X = df[['stETH_supply']]
        y = df['ETH_price']
        self.model.fit(X, y)

    def predict(self, stETH_supply):
        return self.model.predict([[stETH_supply]])[0]

    def save(self, path='models/baseline_model.pkl'):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        joblib.dump(self.model, path)

    def load(self, path='models/baseline_model.pkl'):
        self.model = joblib.load(path)
