"""
Cards Face Up Puzzle.

You are given a full deck of cards, face-down. Four cards are flipped face-up and
randomly re-inserted into the deck.

Write an algorithm which accepts the deck and, using all cards in the deck,
produces at least two collections of cards each containing an equal number of
face-up cards. The catch? The algorithm may *not* look at the cards. (Think about
having to do this by hand, blindfolded.)

* Cards may not be cut in half! (My favorite solution)

Example:
>>> puzzle = new()
>>> stack_one, stack_two = solve(puzzle)
>>> Counter(stack_one)[FaceUp] == Counter(stack_two)[FaceUp]
True

Specify the number of cards flipped:
>>> puzzle = new(30)
>>> stack_one, stack_two = solve(puzzle)
>>> Counter(stack_one)[FaceUp] == Counter(stack_two)[FaceUp]
True
"""
import random
from collections import namedtuple, Counter

###
# Public
###

Puzzle = namedtuple('Puzzle', 'deck flip_count')

# cards are either face-up or face-down, so we'll just use bool values
FaceUp = True
FaceDown = False


def new(flip_count=4):
    """
    Return a shuffled deck (tuple) of 52 Cards, flip_count face-up.

    >>> puzzle = new(7)
    >>> isinstance(puzzle, Puzzle)
    True
    >>> len(puzzle.deck)
    52
    >>> Counter(puzzle.deck)[FaceUp]
    7
    """
    assert flip_count < 52

    deck = [FaceDown for _ in range(52)]
    deck[:flip_count] = _flip(deck[:flip_count])
    random.shuffle(deck)
    return Puzzle(tuple(deck), flip_count)


def solve(puzzle):
    """
    Return two stacks, each with the same number of face-up cards.
    In other words, pull puzzle.flip_count cards off the top and flip 'em!

    >>> puzzle = new()
    >>> stack_one, stack_two = solve(puzzle)
    >>> Counter(stack_one)[FaceUp] == Counter(stack_two)[FaceUp]
    True
    """
    assert isinstance(puzzle, Puzzle)

    top_four, the_rest = _cut(puzzle.deck, puzzle.flip_count)
    return _flip(top_four), the_rest


###
# Internal
###


def _flip(cards):
    """
    Flip each card in the stack.

    >>> _flip((FaceUp, FaceDown,)) == (FaceDown, FaceUp)
    True
    """
    flipped = [not card for card in cards]
    return tuple(flipped)


def _cut(cards, *stack_sizes):
    """
    Return stacks of stack_sizes, and a stack of any left over.

    >>> _cut(range(10), 1, 2, 3)
    ((0,), (1, 2), (3, 4, 5), (6, 7, 8, 9))

    >>> _cut(range(10), 1, 2, 10)
    Traceback (most recent call last):
        ...
    AssertionError
    """
    assert sum(stack_sizes) <= len(cards)

    stacks = []
    index = 0
    for size in stack_sizes:
        stack = tuple(cards[index:index + size])
        stacks.append(stack)
        index += size
    if index < len(cards):
        stack = tuple(cards[index:])
        stacks.append(stack)
    return tuple(stacks)
