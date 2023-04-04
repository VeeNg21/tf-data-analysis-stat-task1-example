import pandas as pd
import numpy as np
from scipy.stats import lognorm

chat_id = 1374771107 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    shape, loc, scale = lognorm.fit(x, floc=0)
    a = np.exp(loc)
    return a
