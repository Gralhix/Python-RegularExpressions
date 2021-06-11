# Regular expressions exercise
# Given a small text substitute a word with a different word


# Import regular expressions.
import re

# Find the name Max in the text bellow.
nomesregex = re.compile(r"Max")

# Will substitute the name "Max" with "João" and print the results.
print(nomesregex.sub("João", "O gato Renato e o cão Max foram andar de balão.\nLonge do chão o cão Max e o gato Renato andaram à bulha e perderam o sapato."))