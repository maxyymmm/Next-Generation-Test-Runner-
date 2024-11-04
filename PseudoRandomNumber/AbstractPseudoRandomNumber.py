from abc import ABC, abstractmethod

class AbstractPseudoRandomNuber(ABC):
    """
    Abstract base class for pseudo-random number generators.
    """

    @abstractmethod
    def generate(self):
        """
        Generates a pseudo-random number.

        @return: int - A pseudo-randomly generated integer value.
        """
        pass