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

    :param flip_count: Number of cards in the deck to flip face-up.
    :type flip_count: int
    :return: Puzzle instance containing the deck of cards and flip_count.
    :rtype: Puzzle

    >>> deck, flip_count = new(flip_count=7)
    >>> len(deck)
    52
    >>> Counter(deck)[FaceUp] == flip_count
    True
    """
    flip_count = min(abs(flip_count), 51) or 1

    deck = [FaceDown for _ in range(52)]
    deck[:flip_count] = _flip(tuple(deck[:flip_count]))
    random.shuffle(deck)
    return Puzzle(tuple(deck), flip_count)


def solve(puzzle):
    """
    Return two stacks, each with the same number of face-up cards.
    In other words, pull puzzle.flip_count cards off the top and flip 'em!

    :param puzzle: Puzzle instance, likely returned by new()
    :type puzzle: Puzzle
    :return: The solution; two stacks (tuple) of cards with the same number of face-up cards.
    :rtype: tuple

    >>> puzzle = new()
    >>> stack_one, stack_two = solve(puzzle)
    >>> Counter(stack_one)[FaceUp] == Counter(stack_two)[FaceUp]
    True
    """
    to_flip, the_rest = _cut(puzzle.deck, puzzle.flip_count)
    return _flip(to_flip), the_rest


###
# Internal
###


def _flip(cards):
    """
    Flip each card in the stack.

    :param cards: A tuple of cards to flip.
    :type cards: tuple
    :return: A tuple of flipped cards FaceUp->FaceDown and FaceDown->FaceUp.
    :rtype: tuple

    >>> _flip((FaceUp, FaceDown,)) == (FaceDown, FaceUp)
    True
    """
    flipped = [not card for card in cards]
    return tuple(flipped)


def _cut(cards, *stack_sizes):
    """
    Return stacks of stack_sizes if possible, and leftovers.
    + stack sizes from the top of the deck of cards
    - stack sizes from the bottom of the deck of cards
    Stack sizes are operated on left-to-right.

    :param cards: A tuple of cards to cut.
    :type cards: tuple
    :param stack_sizes: Sizes of the stacks to be returned.
    :type stack_sizes: int
    :return: stacks of stack_sizes if possible, left to right, and leftovers.
    :rtype: tuple

    >>> stacks = _cut((FaceDown, FaceDown, FaceUp, FaceDown, FaceUp), 0, 1, -3, 5, 10)
    >>> stacks == ((), (FaceDown,), (FaceUp, FaceDown, FaceUp), (FaceDown,))
    True
    """
    stacks = []

    def step(cards, stack_sizes):
        if cards and stack_sizes:
            stack_size, stack_sizes = stack_sizes[0], stack_sizes[1:]

            # cards from top of deck
            if stack_size > 0:
                stacks.append(cards[:stack_size])
                cards = cards[stack_size:]
            # cards from bottom of deck
            elif stack_size < 0:
                stacks.append(cards[stack_size:])
                cards = cards[:stack_size]
            # empty stack
            elif stack_size == 0:
                stacks.append(())

            # step() recursively
            if stack_sizes:
                step(cards, stack_sizes)
            # append any leftover cards
            elif cards:
                stacks.append(cards)

    step(cards, stack_sizes)
    return tuple(stacks)
