"""Simple from-scratch linear models for educational use."""

from typing import Optional
import numpy as np


class LinearRegression:
    """A minimal ordinary least squares implementation."""

    def __init__(self, fit_intercept: bool = True):
        self.fit_intercept = fit_intercept
        self.coef_: Optional[np.ndarray] = None
        self.intercept_: float = 0.0

    def fit(self, X: np.ndarray, y: np.ndarray):
        if self.fit_intercept:
            X = np.column_stack([np.ones(X.shape[0]), X])
        theta, *_ = np.linalg.lstsq(X, y, rcond=None)
        if self.fit_intercept:
            self.intercept_ = float(theta[0])
            self.coef_ = theta[1:]
        else:
            self.coef_ = theta
            self.intercept_ = 0.0
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        if self.fit_intercept:
            return X.dot(self.coef_) + self.intercept_
        return X.dot(self.coef_)
