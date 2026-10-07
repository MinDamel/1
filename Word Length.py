Word = input("Enter a random word: ")
Length = len(Word)

First_character = Word[0]
Last_character = Word[Length - 1]
Middle = Word[1:-1]

Swap = Last_character + Middle + First_character

print(f"Your word: {Word}, has {Length} characters. Swapped version: {Swap}")
