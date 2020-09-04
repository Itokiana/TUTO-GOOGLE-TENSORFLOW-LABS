# https://www.youtube.com/watch?v=fNxaJsNG3-s&list=PLQY2H8rRoyvwLbzbnKJ59NkZvQAW9wLbx&index=1
from tensorflow.keras.preprocessing.text import Tokenizer

sentences = [
    'i love my dog',
    'I, love my cat',
    'You love my dog!'
]

tokenizer = Tokenizer(num_words = 100)
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index
print(word_index)