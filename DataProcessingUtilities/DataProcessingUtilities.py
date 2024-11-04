from DataProcessingUtilities.AbstractDataProcessingUtilities import AbstractDataProcessingUtilities


class DataProcessingUtilities(AbstractDataProcessingUtilities):
    """
    A utility class that provides data processing methods for numerical lists,
    including sorting, calculating the median, and computing the average.
    """

    def sorter(self, numbers):
        """Sorts a list of numbers."""
        return self.quick_sort(numbers)

    def quick_sort(self, numbers):
        """Recursive Quick Sort algorithm."""
        if len(numbers) <= 1:
            return numbers
        else:
            pivot = numbers[0]  # Select the first element as the pivot
            less_than_pivot = [x for x in numbers[1:] if x <= pivot]
            greater_than_pivot = [x for x in numbers[1:] if x > pivot]
            # Recursively sort the partitions and combine with pivot
            return self.quick_sort(less_than_pivot) + [pivot] + self.quick_sort(greater_than_pivot)

    def median(self, numbers):
        """Calculates the median of a list of numbers."""
        sorted_numbers = self.sorter(numbers)
        n = len(sorted_numbers)
        middle = n // 2

        # If the number of elements is odd, return the middle element
        if n % 2 == 1:
            return sorted_numbers[middle]
        # If even, return the average of the two middle elements
        else:
            return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2

    def average(self, numbers):
        """Calculates the average of a list of numbers."""
        return sum(numbers) / len(numbers)