# Next-Generation-Test-Runner-

This project implements a modular setup for generating pseudo-random numbers and performing data processing tasks like sorting, median, and average calculations. The design leverages the factory method pattern, allowing easy integration of alternative implementations for each component, such as different random number generators or sorting algorithms.

## Requirements

- **Python**: 3.11
- **OS**: Ubuntu 22.04 or later

## Installation

Clone the repository:

```bash
git clone https://github.com/maxyymmm/Next-Generation-Test-Runner-
cd Next-Generation-Test-Runner-
```
Start program B:
```bash
python programB.py
```
## Project Structure

### Directories and Key Files

- **`PseudoRandomNumber/`**:
  - `AbstractPseudoRandomNumber.py`: Abstract base class for random number generators.
  - `PseudoRandomNumberFactory.py`: Factory class for creating instances of different random number generators.
  - `PseudoRandomNumberGeneratorInteger.py`: Implementation of a pseudo-random integer generator using a linear congruential generator (LCG) algorithm.

- **`DataProcessingUtilities/`**:
  - `AbstractDataProcessingUtilities.py`: Abstract base class for data processing utilities (e.g., sorting, calculating median and average).
  - `DataProcessingUtilitiesFactory.py`: Factory class for creating instances of different data processing utilities.
  - `DataProcessingUtilities.py`: Implementation of sorting, median, and average calculations.

### Programs

- `programA.py`: A pseudo-random number generator that reads commands from stdin and responds accordingly.
- `programB.py`: A controller that launches `programA.py`, interacts with it, and processes the data received from it.

## Design Pattern: Factory Method

The project uses the **factory method design pattern** in several areas:

- **Random Number Generators**: The `PseudoRandomNumberFactory` class allows for the selection of different number generator types. This setup makes it easy to add more types of generators in the future.
- **Data Processing Utilities**: The factory method is also applied to tools like median, mean, and sorting. If someone wants to use a different algorithm or add new tools, they can easily extend the factory without modifying the core logic.

This design pattern enables flexibility, allowing you to add more options in number generation or data processing tools without altering the main structure of the project.

### Example of Adding New Tools

To add a new tool:

1. Define a new class for the tool, ensuring it inherits from the appropriate abstract base class.
2. Implement the desired functionality.
3. Register the new tool in the corresponding factory dictionary to make it available for use.
