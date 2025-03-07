"""Language models: Bag of words

We can help the computer to make a prediction about languages 
by training a language model on a corpus (a bunch of example text)

Language models are probabilistic computer models of language. 
This models are used to figure out the likelihood that a given sound, letter, 
word or phrase will be used. 

UNIGRAM MODEL
Is a language model known as bag-of-words. What it does is to receive a text 
and return the number of times that a word is repeated
"""

# importing regex and nltk
import re, nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
# importing Counter to get word counts for bag of words
from collections import Counter
# importing part-of-speech function for lemmatization
from nltk.corpus import wordnet
from collections import Counter

looking_glass_text = """
 However, the egg only got larger and larger, and more and more human: when she had come within a few yards of it, she saw that it had eyes and a nose and mouth; and when she had come close to it, she saw clearly that it was HUMPTY DUMPTY himself. It cant be anybody else! she said to herself. Im as certain of it, as if his name were written all over his face.
"""

def get_part_of_speech(word):
    probable_part_of_speech = wordnet.synsets(word)
    pos_counts = Counter()
    pos_counts["n"] = len(  [ item for item in probable_part_of_speech if item.pos()=="n"]  )
    pos_counts["v"] = len(  [ item for item in probable_part_of_speech if item.pos()=="v"]  )
    pos_counts["a"] = len(  [ item for item in probable_part_of_speech if item.pos()=="a"]  )
    pos_counts["r"] = len(  [ item for item in probable_part_of_speech if item.pos()=="r"]  )

    most_likely_part_of_speech = pos_counts.most_common(1)[0][0]
    return most_likely_part_of_speech
text = looking_glass_text

cleaned = re.sub('\W+', ' ', text).lower()
tokenized = word_tokenize(cleaned)

stop_words = stopwords.words('english')
filtered = [word for word in tokenized if word not in stop_words]

normalizer = WordNetLemmatizer()
normalized = [normalizer.lemmatize(token, get_part_of_speech(token)) for token in filtered]

bag_of_looking_glass_words = Counter(normalized)
print(bag_of_looking_glass_words)

