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
* Puzzles are fun. Solve each one yourself before reading the solution.
* Puzzles are great interview questions: discuss solutions, optimizations, corner cases, etc.
* Solutions can be improved. Feel free to fork and send a pull request :)
* Please send me new puzzle descriptions!

A summary of each included puzzle follows ...

Sentence Word Scramble
----------------------
You are given a sentence where each word's character order is shuffled and spaces
between words have been removed.
* Example: "yarmdahaeltltibaml"

You are given a list of possible words in the sentence.
* The dictionary includes, at a minimum, ("little", "a", "had", "lamb", "mary")

Write an algorithm which accepts the scrambled sentence and the list of words to
produce the original sentence with spaces and un-shuffled words.

Cards Face Up
-------------
(coming soon)
