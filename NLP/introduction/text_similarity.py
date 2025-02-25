"""Text similarity

Addressing word similarity and misspelling for spellcheck or autocorrect often involves considering the Levenshtein disntance or minimal 
edit distance between two words. The distance is calculated through the minimum number of insertions, deletions, and substitutions that would 
need to occur for one word to become another

Phonetic similarity is also a major challenge within speech recognition. More advanced autocorrect and spelling correction technology additionally
considers key distance on a keyboard and phonetic similarity. 
"""
import nltk
# NLTK has a built-in function
# to check Levenshtein distance:
from nltk.metrics import edit_distance

def print_levenshtein(string1, string2):
  print("The Levenshtein distance from '{0}' to '{1}' is {2}!".format(string1, string2, edit_distance(string1, string2)))

three_away_from_code = "coats"

two_away_from_chunk = "punk"

print_levenshtein("code", three_away_from_code)
print_levenshtein("chunk", two_away_from_chunk)