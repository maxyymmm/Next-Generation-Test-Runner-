from abc import ABC, abstractmethod

class AbstractDataProcessingUtilities(ABC):
    """
    Abstract base class for data processing utilities.
    """

    @abstractmethod
    def sorter(self, numbers):
        """
        Sorts a list of numbers in ascending order.

        @param numbers: list - A list of numerical values to be sorted.
        @return: list - A sorted list of numbers in ascending order.
        """
        pass

    @abstractmethod
    def median(self, numbers):
        """
        Calculates the median value from a list of numbers.

        @param numbers: list - A list of numerical values from which to calculate the median.
        @return: float - The median value of the list.
        """
        pass

    @abstractmethod
    def average(self, numbers):
        """
        Calculates the average (mean) value from a list of numbers.

        @param numbers: list - A list of numerical values from which to calculate the average.
        @return: float - The average (mean) value of the list.
        """
        pass