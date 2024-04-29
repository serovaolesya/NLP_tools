from collections import Counter
import re

import spacy

nlp = spacy.load("ru_core_news_sm")
lemmatizer = nlp.get_pipe("lemmatizer")

text = """
Вставьте сюда свой текст, чтобы лемматизировать слова и подсчитать частоту. Стоп-слова не будут подсчитываться.
"""
lower_cased_text = text.lower()
cleaned_text = re.sub(r'[^\w\s]', '', text)

doc = nlp(cleaned_text)
print(f'Лемматизированные слова: {[token.lemma_ for token in doc if not token.is_stop and token.is_alpha]}')
words_list = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
freq = Counter(words_list)
print(freq)