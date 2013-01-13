puzzles
=======
A growing collection of interesting programming puzzles (and solutions).

All puzzles have, at a minimum, the following public interface:

    from puzzles import somepuzzle
    puzzle = somepuzzle.new(inputs ...)
    solution = somepuzzle.solve(puzzle)

solve() will return an iterable, or a generator if there are infinite or very many
solutions.

**Thoughts:**
* Puzzles are the most fun when solved yourself before reading a solution.
* Puzzles make great interview questions: discuss solutions, optimizations, corner cases, etc.
* Solutions can be always be improved. Please fork and send a pull request :)
* Please send new puzzle descriptions!

A summary of each included puzzle follows ...

Sentence Word Scramble
----------------------
You are given a sentence where each word's character order is shuffled and spaces
between words have been removed.
* Example: "yarmdahaeltltibaml"

You are given a list of possible words in the sentence.
* The words include, at a minimum, the words in the sentence: ("little", "a", "had", "lamb", "mary")

Write an algorithm which accepts the scrambled sentence and the list of words to
produce the original sentence with spaces and un-shuffled words.
* "yarmdahaeltltibaml" + ("little", "a", "had", "lamb", "mary") -> "mary had a little lamb"

Cards Face Up
-------------
You are given a full deck of cards, face-down. Four cards are flipped face-up and
randomly re-inserted into the deck.

Write an algorithm which accepts the shuffled deck and, using all cards, produces
at least two collections of cards each containing an equal number of face-up
cards. The catch? The algorithm may *not* look at the orientation of the cards.
(Think about having to do this by hand, blindfolded.)

* The deck of cards may not be cut in half (as in, with a hatchet)! *My favorite solution.*
