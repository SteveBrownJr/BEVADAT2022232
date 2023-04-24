import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt


class LinearRegression:
    def __init__(self, epochs: int = 1000, lr: float = 1e-3):
        self.epochs = epochs
        self.lr = lr
        self.m = 0
        self.c = 0
        self.losses = []


    def fit(self, X: np.array, y: np.array):
        n = float(len(X)) 
        
        for i in range(self.epochs): 
            y_pred = self.m * X + self.c

            residuals = y - y_pred
            loss = np.sum(residuals ** 2)
            self.losses.append(loss)
            D_m = (-2/n) * sum(X * residuals)
            D_c = (-2/n) * sum(residuals)
            self.m = self.m - self.lr * D_m 
            self.c = self.c - self.lr * D_c
        return self.losses

    def predict(self, X):
        return self.m * X + self.c
    
    def evaluate(self, X, y):
        pred = self.predict(X)
        return np.mean((pred - y)**2)