import os
import importlib


def test_package_import():
    mod = importlib.import_module("ml_detective_academy")
    assert hasattr(mod, "__version__")


def test_linear_model_smoke():
    mod = importlib.import_module("ml_detective_academy.linear_model")
    LR = mod.LinearRegression
    import numpy as np

    X = np.array([[1.0], [2.0], [3.0]])
    y = np.array([2.0, 4.0, 6.0])
    model = LR()
    model.fit(X, y)
    preds = model.predict(X)
    assert preds.shape == y.shape
