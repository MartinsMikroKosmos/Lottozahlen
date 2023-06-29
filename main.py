import random


class Lotto:
    message_length = 60
    description = ""

    def __init__(self):
        """Lotto-Klasse"""

    def get_numeric_input(self, message=""):
        while True:
            user_input = input(message)

            if user_input.isnumeric():
                return int(user_input)
            else:
                print("Bitte eine Zahl angeben")
                continue

    def print_welcome_message(self):
        print("Lottozahlen Generator".center(self.message_length))

    def print_lotto_numbers(self, numbers):
        print("Deine Zahlen sind:", end=" ")
        for number in numbers:
            if isinstance(number, list):
                super_numbers = ", ".join(str(n) for n in number)
                print(f"Superzahlen: {super_numbers}")
            else:
                print(number, end=" ")
        print()

    def print_description(self):
        print("\n" + self.description.center(self.message_length) + "\n")

    # Basic run method
    def run(self):
        self.print_welcome_message()

        while True:
            self.print_description()

            choice = self.get_numeric_input("Wähle eine Lotterie aus! [1] 6 aus 49, [2] EuroLotto: ")

            if choice == 1:
                game = Lotto6aus49()
            elif choice == 2:
                game = EuroLotto()
            else:
                print("Bitte wähle eine richtige Lotterie aus")
                continue

            num_sets = self.get_numeric_input("Wie viele Lotterie-Sätze möchtest du generieren? ")

            for _ in range(num_sets):
                lotto_numbers = game.generate_lotto_numbers()
                self.print_lotto_numbers(lotto_numbers)

            repeat = input("Möchtest du weitere Lotterie-Sätze generieren? (ja/nein): ")
            if repeat.lower() != "ja":
                break


class Lotto6aus49(Lotto):
    description = "Willkommen bei 6 aus 49!"

    def __init__(self):
        super().__init__()

    def generate_lotto_numbers(self):
        lottoZahlen = list(range(1, 50))
        superZahlen = list(range(1, 11))

        lottoZahlen_gewinn = random.sample(lottoZahlen, 6)
        superZahlen_gewinn = random.sample(superZahlen, 1)

        lottoZahlen_gewinn.sort()
        superZahlen_gewinn.sort()

        lottoZahlen_gewinn.append(superZahlen_gewinn)

        return lottoZahlen_gewinn


class EuroLotto(Lotto):
    description = "Willkommen bei EuroLotto!"

    def __init__(self):
        super().__init__()

    def generate_lotto_numbers(self):
        lottoZahlen = list(range(1, 51))
        superZahlen = list(range(1, 11))

        lottoZahlen_gewinn = random.sample(lottoZahlen, 5)
        superZahlen_gewinn = random.sample(superZahlen, 2)

        lottoZahlen_gewinn.sort()
        superZahlen_gewinn.sort()

        lottoZahlen_gewinn.append(superZahlen_gewinn)

        return lottoZahlen_gewinn


if __name__ == "__main__":
    game = Lotto()
    game.run()
