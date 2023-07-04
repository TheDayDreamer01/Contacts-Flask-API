from string import (
    ascii_lowercase,
    ascii_uppercase,
    digits,
    punctuation
)
from random import choice


def keyGenerator(length : int) -> str:
    SYMBOLS : str = ascii_lowercase + ascii_uppercase + digits + punctuation
    pattern = "".join([ choice(SYMBOLS) for i in range(length) ])
    return pattern