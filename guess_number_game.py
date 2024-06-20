import random


class GuessNumberGame:
    def __init__(self):
        self.number_to_guess = random.randint(1, 10)
        self.max_attempts = 3
        self.attempts = 0

    def prompt_guess(self):
        try:
            guess = int(input(f"Próba {self.attempts + 1}: "))
        except ValueError:
            print("Proszę wprowadzić poprawną liczbę.")
            return None
        if guess < 1 or guess > 10:
            print("Liczba musi być w przedziale od 1 do 10.")
            return None
        return guess

    def play(self):
        print("Zgadnij liczbę od 1 do 10. Masz 3 próby.")
        while self.attempts < self.max_attempts:
            guess = self.prompt_guess()
            if guess is None:
                continue

            self.attempts += 1

            if guess == self.number_to_guess:
                print(f"Gratulacje! Zgadłeś liczbę {self.number_to_guess} w {self.attempts} próbie!")
                return
            elif guess < self.number_to_guess:
                print("Liczba do zgadnięcia jest większa.")
            else:
                print("Liczba do zgadnięcia jest mniejsza.")

        print(f"Niestety, nie udało się zgadnąć liczby. Liczba do zgadnięcia to {self.number_to_guess}.")


if __name__ == "__main__":
    game = GuessNumberGame()
    game.play()
