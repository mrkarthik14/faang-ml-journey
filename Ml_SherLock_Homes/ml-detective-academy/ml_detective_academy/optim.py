"""Simple optimization utilities (gradient descent)"""

import numpy as np
from typing import Callable


def gradient_descent(
    grad_fn: Callable[[np.ndarray], np.ndarray],
    init: np.ndarray,
    lr: float = 1e-3,
    steps: int = 1000,
):
    theta = init.copy()
    for _ in range(steps):
        g = grad_fn(theta)
        theta = theta - lr * g
    return theta
