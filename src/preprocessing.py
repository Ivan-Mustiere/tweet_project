import re
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def clean_text(text: str) -> str:
    if not isinstance(text, str) or text.strip() == "":
        return ""

    # Mise en minuscule
    text = text.lower()

    # Suppression des URLs
    text = re.sub(r'http\S+|www.\S+', '', text)

    # Suppression des mentions et hashtags
    text = re.sub(r'@\w+|#\w+', '', text)

    # Suppression de la ponctuation et des chiffres
    text = re.sub(r'[%s]' % re.escape(string.punctuation), ' ', text)
    text = re.sub(r'\d+', '', text)

    # Tokenisation
    tokens = word_tokenize(text)

    # Suppression des mots courts et des stopwords + stemming
    cleaned = [
        stemmer.stem(word)
        for word in tokens
        if word not in stop_words and len(word) > 2
    ]

    return ' '.join(cleaned)
