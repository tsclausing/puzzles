"""
Test Sentence Word Scramble
"""
import doctest
import unittest

from collections import Counter

from puzzles import sentencewordscramble
from puzzles.sentencewordscramble import new, solve, Puzzle, _sanitize_sentence


class SentenceWordScramble(unittest.TestCase):

    def test_doctest(self):
        self.assertFalse(doctest.testmod(sentencewordscramble).failed)

    def test_new(self):
        original = 'mary had a little lamb'
        puzzle = new(original)
        self.assertIsInstance(puzzle, Puzzle)
        # all original letters accounted for
        self.assertEqual(Counter(puzzle.sentence), Counter(original.replace(' ', '')))
        # all original words accounted for
        self.assertEqual(set(original.split()), puzzle.words)

        # TODO: Test with more_words

    def test_solve(self):
        # TODO
        pass

    def test_sanitize_sentence(self):
        # TODO
        pass
