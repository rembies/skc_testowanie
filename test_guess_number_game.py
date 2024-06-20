import pytest
from unittest.mock import patch
import io
from contextlib import redirect_stdout
from guess_number_game import GuessNumberGame


class TestGuessNumberGame:
    @patch('builtins.input', side_effect=[3, 5, 7])
    @patch('random.randint', return_value=6)
    def test_przekroczono_ilosc_prob(self, mock_randint, mock_input):
        game = GuessNumberGame()
        with io.StringIO() as buf, redirect_stdout(buf):
            game.play()
            output = buf.getvalue()
        assert "Niestety, nie udało się zgadnąć liczby. Liczba do zgadnięcia to 6." in output

    @patch('builtins.input', side_effect=[6])
    @patch('random.randint', return_value=6)
    def test_odgadnieto_w_pierwszej_probie(self, mock_randint, mock_input):
        game = GuessNumberGame()
        with io.StringIO() as buf, redirect_stdout(buf):
            game.play()
            output = buf.getvalue()
        assert "Gratulacje! Zgadłeś liczbę 6 w 1 próbie!" in output

    @patch('builtins.input', side_effect=[1, 2, 3])
    @patch('random.randint', return_value=5)
    def test_nie_odgadnieto_liczby(self, mock_randint, mock_input):
        game = GuessNumberGame()
        with io.StringIO() as buf, redirect_stdout(buf):
            game.play()
            output = buf.getvalue()
        assert "Niestety, nie udało się zgadnąć liczby. Liczba do zgadnięcia to 5." in output

    @patch('builtins.input', side_effect=[1, 2, 5])
    @patch('random.randint', return_value=5)
    def test_odgadnieto_liczbe_w_ostatniej_probie(self, mock_randint, mock_input):
        game = GuessNumberGame()
        with io.StringIO() as buf, redirect_stdout(buf):
            game.play()
            output = buf.getvalue()
        assert "Gratulacje! Zgadłeś liczbę 5 w 3 próbie!" in output

    @patch('builtins.input', side_effect=['a', 11, 6])
    @patch('random.randint', return_value=6)
    def test_komunikaty_wyswietlane_w_grze(self, mock_randint, mock_input):
        game = GuessNumberGame()
        with io.StringIO() as buf, redirect_stdout(buf):
            game.play()
            output = buf.getvalue()
        assert "Proszę wprowadzić poprawną liczbę." in output
        assert "Liczba musi być w przedziale od 1 do 10." in output
        assert "Gratulacje! Zgadłeś liczbę 6 w 1 próbie!" in output


if __name__ == "__main__":
    pytest.main()
