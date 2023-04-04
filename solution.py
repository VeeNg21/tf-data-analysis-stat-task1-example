import pandas as pd
import numpy as np


chat_id = 1374771107 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    N = len(x)
    a = (1 / N) * np.sum(np.log(x)) - (1 / (2 * N)) * np.sum(np.log(x))**2
    return a
