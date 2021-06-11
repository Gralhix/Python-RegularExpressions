# Regular expressions exercise
# Given a small text substitute a word with a different word


# Import regular expressions.
import re

# Find the name Max, whether it's written as "Max" or "max".
nomesregex = re.compile(r"Max", re.IGNORECASE)

# Will substitute the name "Max" and "max" with "João" and print the results.
print(nomesregex.sub("João", "O gato Renato e o cão max foram andar de balão.\nLonge do chão o cão Max e o gato Renato andaram à bulha e perderam o sapato."))
