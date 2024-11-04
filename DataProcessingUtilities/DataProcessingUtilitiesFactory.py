from DataProcessingUtilities.AbstractDataProcessingUtilities import AbstractDataProcessingUtilities
from DataProcessingUtilities.DataProcessingUtilities import DataProcessingUtilities


class DataProcessingUtilitiesFactory:
    """
        Factory class for creating instances of data processing utilities.

        This class provides a static method to create instances of data processing
        utility classes based on the specified type.
    """
    DataProcessingUtilitiesType = {
        "defaultUtilities": DataProcessingUtilities,
    }

    @staticmethod
    def create_utilities(utility_type: str) -> AbstractDataProcessingUtilities:
        if utility_type not in DataProcessingUtilitiesFactory.DataProcessingUtilitiesType:
            message = (f"There is no Utility Type class for {utility_type}. "
                       f"Available types are: {list(DataProcessingUtilitiesFactory.DataProcessingUtilitiesType.keys())}")
            raise RuntimeError(message)

        utility_class = DataProcessingUtilitiesFactory.DataProcessingUtilitiesType[utility_type]
        return utility_class()