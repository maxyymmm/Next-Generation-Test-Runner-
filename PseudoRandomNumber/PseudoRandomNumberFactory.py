from PseudoRandomNumber.AbstractPseudoRandomNumber import AbstractPseudoRandomNumber
from PseudoRandomNumber.PseudoRandomNumberGeneratorInteger import PseudoRandomNumberGeneratorInteger


class PseudoRandomNumberGeneratorFactory:
    """
        Factory class for creating instances of pseudo-random number generators.

        This class provides a method to create instances of pseudo-random number
        generator classes based on the specified type.
    """
    PseudoRandomNumberGeneratorType={
        "integer": PseudoRandomNumberGeneratorInteger,
    }

    @staticmethod
    def get_pseudo_random_number_generator_type(generator_type: str) -> AbstractPseudoRandomNumber:
        if generator_type not in PseudoRandomNumberGeneratorFactory.PseudoRandomNumberGeneratorType:
            message = (f"There is no Generator Type class for {generator_type}."
                       f"There are Generator Type classes only for {PseudoRandomNumberGeneratorFactory.PseudoRandomNumberGeneratorType.keys()} ")
            raise RuntimeError(message)

        generator_type_class = PseudoRandomNumberGeneratorFactory.PseudoRandomNumberGeneratorType[generator_type]
        return generator_type_class()