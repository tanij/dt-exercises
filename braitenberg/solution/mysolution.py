from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")
    h, w = shape
    half = int(w / 2)
    hh = int(h / 3)

    res[:hh, 0:half] = 1
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")
    h, w = shape
    half = int(w / 2)
    hh = int(h / 3)

    res[:hh, half:] = 1
    return res
