import unittest
from core.game_logic import *
from utils.validators import check_winnings

class TestCheckWinnings(unittest.TestCase):

    def _assert_winnings(self, columns, lines, bet, multipliers, expected_amount, expected_lines):
       
        winnings, winning_lines = check_winnings(columns, lines, bet, multipliers)
        self.assertEqual(winnings, expected_amount)
        self.assertEqual(winning_lines, expected_lines)

    def test_all_lines_win(self):
        columns = [
            ['A', 'B', 'C'],
            ['A', 'B', 'C'],
            ['A', 'B', 'C']
        ]
        bet = 10
        lines = 3
        multipliers = {"A": 5, "B": 4, "C": 3}
        expected = 5*10 + 4*10 + 3*10
        self._assert_winnings(columns, lines, bet, multipliers, expected, [1, 2, 3])

    def test_some_lines_win(self):
        columns = [
            ['A', 'B', 'C'],
            ['A', 'X', 'C'],
            ['A', 'Y', 'C']
        ]
        bet = 5
        lines = 3
        multipliers = {"A": 5, "B": 4, "C": 3}
        expected = 5*5 + 3*5
        self._assert_winnings(columns, lines, bet, multipliers, expected, [1, 3])

    def test_no_lines_win(self):
        columns = [
            ['A', 'B', 'C'],
            ['B', 'C', 'A'],
            ['C', 'A', 'B']
        ]
        bet = 10
        lines = 3
        multipliers = {"A": 5, "B": 4, "C": 3}
        self._assert_winnings(columns, lines, bet, multipliers, 0, [])

    def test_partial_lines(self):
        columns = [
            ['A', 'B', 'C'],
            ['A', 'X', 'C'],
            ['A', 'Y', 'Z']
        ]
        bet = 10
        lines = 1  # Only line 1 is tested
        multipliers = {"A": 5, "B": 4, "C": 3, "Z": 1}
        self._assert_winnings(columns, lines, bet, multipliers, 5 * 10, [1])

    def test_spin_dimensions(self):
        result = get_slot_machine_spin(3, 3, {"A": 4, "B": 4})
        self.assertEqual(len(result), 3)
        for col in result:
            self.assertEqual(len(col), 3)

    def test_symbols_are_valid(self):
        allowed = {"A": 2, "B": 2, "C": 2}
        result = get_slot_machine_spin(3, 3, allowed)
        for col in result:
            for val in col:
                self.assertIn(val, allowed)
