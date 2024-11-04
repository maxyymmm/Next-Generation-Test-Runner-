import subprocess

from DataProcessingUtilities.DataProcessingUtilitiesFactory import DataProcessingUtilitiesFactory
from PseudoRandomNumber.PseudoRandomNumberFactory import PseudoRandomNumberGeneratorFactory


def main():
    # Launch Program A as a separate process
    process = subprocess.Popen(
        ["python3", "programA.py"],  # Change to "python" if using Windows
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True
    )

    process.stdin.write("Hi\n")
    process.stdin.flush()
    response = process.stdout.readline().strip()
    if response != "Hi":
        print("Program A did not respond correctly to 'Hi'.")
        process.terminate()
        return

    # Retrieve 100 random numbers
    random_numbers = []
    for _ in range(100):
        process.stdin.write("GetRandom\n")
        process.stdin.flush()
        response = process.stdout.readline().strip()
        try:
            random_numbers.append(int(response))
        except ValueError:
            print("Invalid response received for 'GetRandom'.")
            process.terminate()
            return

    process.stdin.write("Shutdown\n")
    process.stdin.flush()
    process.wait()

    pseudo_nums_generator = PseudoRandomNumberGeneratorFactory.get_pseudo_random_number_generator_type(
        generator_type="integer")
    pseudo_nums_list = []
    for _ in range(100):
        pseudo_num = pseudo_nums_generator.generate()
        pseudo_nums_list.append(pseudo_num)

    print("List of pseudo numbers:", pseudo_nums_list)

    data_utilities = DataProcessingUtilitiesFactory.create_utilities("defaultUtilities")

    sorted_nums = data_utilities.sorter(pseudo_nums_list)
    print("Sorted random numbers:", sorted_nums)

    median = data_utilities.median(pseudo_nums_list)
    average = data_utilities.average(pseudo_nums_list)
    print(f"Median: {median:.2f}")
    print(f"Average: {average:.2f}")


if __name__ == "__main__":
    main()
