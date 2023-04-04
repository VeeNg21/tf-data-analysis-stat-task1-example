import pandas as pd
import numpy as np
from scipy.stats import lognorm

chat_id = 1374771107 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    mu = np.mean(np.log(x))
    sigma = np.std(np.log(x))
    a_hat = np.exp(mu - sigma**2/2)
    return a_hat
