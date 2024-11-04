import sys

from PseudoRandomNumber.PseudoRandomNumberFactory import PseudoRandomNumberGeneratorFactory


class PseudoRandomNumberGenerator:
    def __init__(self):
        self.commands = {
            "Hi": self.respond_hi,
            "GetRandom": self.get_random_number,
            "Shutdown": self.shutdown,
        }
        self.running = True

    def respond_hi(self):
        print("Hi")
        sys.stdout.flush()

    def get_random_number(self):
        random_gen = PseudoRandomNumberGeneratorFactory().get_pseudo_random_number_generator_type(
            generator_type="integer")
        print(random_gen.generate())
        sys.stdout.flush()

    def shutdown(self):
        self.running = False

    def handle_command(self, command):
        action = self.commands.get(command)
        if action:
            action()
        else:
            pass  # Ignore unknown commands

    def run(self):
        while self.running:
            command = sys.stdin.readline().strip()
            self.handle_command(command)


if __name__ == "__main__":
    generator = PseudoRandomNumberGenerator()
    generator.run()