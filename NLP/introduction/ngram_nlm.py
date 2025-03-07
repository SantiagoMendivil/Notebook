"""Language models: N-Gram and NLM

In the bag-of-words case the language model will only consider 
the number of times that a word is repeated. And for the n-gram 
model, it considers a sequence of some number units and calculates
the probability of each unit in a body of language given. 

Because of that reason, the probability of predicting is larger. 

TROUBLES
1. Sometimes the language model can find words that it hasn't seen before. 
This can be solved by using the bag-of-words model or a tactic known as 
language smoothing.
2. To be more accurately with the prediction, we want that "n" (the length) 
is going to be as large as possible. On the other hand, as the sequence grows
the number of examples within your training shrinks. Too few examples won't have enough data. 
"""

import nltk, re
from nltk.tokenize import word_tokenize
# importing ngrams module from nltk
from nltk.util import ngrams
from collections import Counter

looking_glass_full_text = "Lookingglass full text for words that contain spaces separated by spaces"

cleaned = re.sub('\W+', ' ', looking_glass_full_text).lower()
tokenized = word_tokenize(cleaned)

looking_glass_bigrams = ngrams(tokenized, 2)
looking_glass_bigrams_frequency = Counter(looking_glass_bigrams)

looking_glass_trigrams = ngrams(tokenized, 3)
looking_glass_trigrams_frequency = Counter(looking_glass_trigrams)

looking_glass_ngrams = ngrams(tokenized, 5)
looking_glass_ngrams_frequency = Counter(looking_glass_ngrams)

print("Looking Glass Bigrams:")
print(looking_glass_bigrams_frequency.most_common(10))

print("\nLooking Glass Trigrams:")
print(looking_glass_trigrams_frequency.most_common(10))

print("\nLooking Glass n-grams:")
print(looking_glass_ngrams_frequency.most_common(10))