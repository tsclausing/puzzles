"""
Sentence Word Scramble Puzzle.

Description:
============
You have a sentence with several words with spaces removed and the words have
their character order shuffled. You have a dictionary to lookup. Write an
algorithm to produce the original sentence back with spaces and words with normal
character order.

Examples:
--------
>>> 'mary had a little lamb' in solve(puzzle("Mary had a little lamb."))
True

Test this 100 times to ensure backtracking:
>>> solutions = [solve(puzzle("Mary had a little lamb.")) for _ in range(100)]
>>> all(map(lambda solution: 'mary had a little lamb' in solution, solutions))
True

Add more words to Puzzle to increase complexity:
>>> solutions = solve(puzzle('Mary had a little lamb.', ('yarm', 'ahad', 'lit', 'balm')))
>>> 'mary had a little lamb' in solutions
True

Author: Scot Clausing
"""
import re
import random
import collections

###
# Public
###

Puzzle = collections.namedtuple('Puzzle', 'words sentence')


def puzzle(sentence, more_words=()):
    """
    Return a 'Sentence Word Scramble' Puzzle created from the sentence.
    """
    sentence = _sanitize_sentence(sentence)
    words = sentence.split()

    puzzle_sentence = ''
    for word in words:
        word = [c for c in word]
        random.shuffle(word)
        puzzle_sentence += ''.join(word)

    return Puzzle(set(words) | set(more_words), puzzle_sentence)


def solve(puzzle):
    """
    Return all solutions to the puzzle.
    """
    assert isinstance(puzzle, Puzzle)

    # {index: [word, ...]}
    possibilities_at = collections.defaultdict(list)

    # find possible positions of each word in the sentence
    for word in puzzle.words:
        sorted_word = sorted([c for c in word])
        for index in range(len(puzzle.sentence) - len(word) + 1):
            sorted_candidate = sorted(puzzle.sentence[index:index + len(word)])
            if sorted_candidate == sorted_word:
                possibilities_at[index].append(word)

    solutions = []

    # recursively evaluate each possibility, appending to solutions when found
    def step(partial_solution=None):
        partial_solution = partial_solution or []
        index = sum(map(len, partial_solution))

        # step forward to next possibility
        if possibilities_at[index]:
            for word in possibilities_at[index]:
                partial_solution.append(word)
                # recursive step()
                if not step(partial_solution):
                    partial_solution.pop()

        # is the partial solution a full solution?
        elif index == len(puzzle.sentence):
            solutions.append(' '.join(partial_solution))

        # step back
        return False

    step()
    return tuple(solutions)


###
# Internal
###


def _sanitize_sentence(sentence):
    """
    Remove invalid characters from the sentence.

    >>> _sanitize_sentence(" Mary had a hot-rod, whose seat's were   white as snow.\t")
    'mary had a hot-rod whose seats were white as snow'
    """
    invalid_chars = re.compile(r'[^a-zA-Z\- ]')
    spaces = re.compile(r'[ ]+')

    sentence = invalid_chars.sub('', sentence)
    sentence = spaces.sub(' ', sentence)
    sentence = sentence.strip().lower()
    return sentence

