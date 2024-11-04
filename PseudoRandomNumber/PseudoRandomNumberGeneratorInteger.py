import time
from PseudoRandomNumber.AbstractPseudoRandomNumber import AbstractPseudoRandomNumber

class PseudoRandomNumberGeneratorInteger(AbstractPseudoRandomNumber):
    """
    A pseudo-random number generator that generates integers
    """

    def __init__(self, seed=None):
        """
        Initializes the generator with a given seed or uses the current time if no seed is provided.

        The LCG algorithm parameters `a`, `c`, and `m` are constants chosen for a 32-bit output range.

        @param seed: int or None - The initial seed value for the generator. If None, the current time is used.
        """
        self.seed = seed if seed is not None else int(time.time())
        self.a = 1664525
        self.c = 1013904223
        self.m = 2**32  # Output range (32-bit)

    def generate(self):
        """
        Generates a pseudo-random integer within the range [0, 1000].

        Uses the LCG formula: X_{n+1} = (a * X_n + c) % m to update the seed and
        produce a new pseudo-random integer. The result is then limited to the range [0, 1000]
        using modulo 1001.

        @return: int - A pseudo-random integer between 0 and 1000.
        """

        # LCG formula: X_{n+1} = (a * X_n + c) % m
        self.seed = (self.a * self.seed + self.c) % self.m
        # Return the number within the range from 0 to 1000 by using modulo 1001
        return self.seed % 1001