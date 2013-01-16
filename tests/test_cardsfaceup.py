"""
Test Cards Face Up Puzzle
"""
import doctest
import unittest

from collections import Counter

from puzzles import cardsfaceup
from puzzles.cardsfaceup import new, solve, Puzzle, FaceUp, FaceDown, _flip, _cut


class CardsFaceUp(unittest.TestCase):

    def test_doctest(self):
        self.assertFalse(doctest.testmod(cardsfaceup).failed)

    def test_new(self):
        # default flip_count
        puzzle = new()
        self.assertIsInstance(puzzle, Puzzle)
        self.assertEqual((len(puzzle.deck), puzzle.flip_count), (52, 4))
        self.assertEqual(Counter(puzzle.deck)[FaceUp], 4)

        # custom flip_count
        puzzle = new(flip_count=10)
        self.assertEqual((len(puzzle.deck), puzzle.flip_count), (52, 10))
        self.assertEqual(Counter(puzzle.deck)[FaceUp], 10)

        # flip_count >= 52 -> 51
        puzzle = new(flip_count=100)
        self.assertEqual((len(puzzle.deck), puzzle.flip_count), (52, 51))
        self.assertEqual(Counter(puzzle.deck)[FaceUp], 51)

        # flip_count <= 1 -> abs(flip_count)
        puzzle = new(flip_count=-10)
        self.assertEqual((len(puzzle.deck), puzzle.flip_count), (52, 10))
        self.assertEqual(Counter(puzzle.deck)[FaceUp], 10)

        # flip_count == 0 -> 1
        puzzle = new(flip_count=0)
        self.assertEqual((len(puzzle.deck), puzzle.flip_count), (52, 1))
        self.assertEqual(Counter(puzzle.deck)[FaceUp], 1)

    def test_solve(self):
        # solve for all allowed flip_count values
        for flip_count in range(1, 52):
            puzzle = new(flip_count)
            stack_one, stack_two = solve(puzzle)
            self.assertEqual(Counter(stack_one)[FaceUp], Counter(stack_two)[FaceUp])

    def test_flip(self):
        cards = (FaceUp, FaceDown)
        self.assertEqual(_flip(cards), (FaceDown, FaceUp))

    def test_cut(self):
        cards = (FaceUp, FaceDown, FaceUp, FaceUp)

        # stack sizes sum to len(cards)
        self.assertEqual(_cut(cards, 2, 1, 1), ((FaceUp, FaceDown), (FaceUp,), (FaceUp,)))

        # stack sizes leave remainder
        self.assertEqual(_cut(cards, 2, 1), ((FaceUp, FaceDown), (FaceUp,), (FaceUp,)))

        # stack sizes sum > len(cards)
        self.assertEqual(_cut(cards, 1, 10), ((FaceUp,), (FaceDown, FaceUp, FaceUp)))

        # too many stack sizes and sum > len(cards)
        self.assertEqual(_cut(cards, 1, 10, 10, 10), ((FaceUp,), (FaceDown, FaceUp, FaceUp)))

        # stack sizes include 0
        self.assertEqual(_cut(cards, 1, 0, 10), ((FaceUp,), (), (FaceDown, FaceUp, FaceUp)))

        # stack sizes include negative
        self.assertEqual(_cut(cards, -1, -10), ((FaceUp,), (FaceUp, FaceDown, FaceUp)))
