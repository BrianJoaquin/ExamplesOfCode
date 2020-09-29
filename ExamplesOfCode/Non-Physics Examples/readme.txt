RPS:

A simple "Rock, Paper, Scissors" game.
------------------------------------------------------------------------
Persistence:

Based on the problem from https://edabit.com/challenge/5ou6SKDtFRZugbpda

The additive persistence of an integer, n, is the number of times you have to replace n with the sum of its digits until n becomes a single digit integer.
The multiplicative persistence of an integer, n, is the number of times you have to replace n with the product of its digits until n becomes a single digit integer.

Create two functions that take an integer as an argument and:
	1. Return its additive persistence.
	2. Return its multiplicative persistence.
-----------------------------------------------------------------------------------------------------------------------------------------------------------
Polybius Cypher:

Based on the problem from https://edabit.com/challenge/2C3gtb4treAFyWJMg

The Polybius Square cipher is a simple substitution cipher that makes use of a 5x5 square grid. 
The letters A-Z are written into the grid, with "I" and "J" typically sharing a slot (as there are 26 letters and only 25 slots).
To encipher a message, each letter is merely replaced by its row and column numbers in the grid.
Create a function that takes a plaintext or ciphertext message, and returns the corresponding ciphertext or plaintext.