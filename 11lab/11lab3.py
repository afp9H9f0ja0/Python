import nltk
from nltk.corpus import gutenberg
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import string

print("Завантаження баз даних NLTK...")
nltk.download('gutenberg')
nltk.download('stopwords')
nltk.download('punkt')

file_id = 'austen-persuasion.txt'
words = gutenberg.words(file_id)

print(f"\n--- Аналіз тексту: {file_id} ---")

total_words = len(words)
print(f"Загальна кількість слів (токенів) у тексті: {total_words}")

fdist_raw = FreqDist(w.lower() for w in words)

top_10_raw = fdist_raw.most_common(10)
print("\n10 найбільш вживаних слів (із пунктуацією та стоп-словами):")
print(top_10_raw)

words_raw, counts_raw = zip(*top_10_raw)

plt.figure(figsize=(12, 6))
plt.bar(words_raw, counts_raw, color='skyblue')
plt.title("Топ-10 слів у тексті (без очищення)")
plt.xlabel("Слова")
plt.ylabel("Кількість")
plt.show()


print("\nВиконується очищення тексту...")

stop_words = set(stopwords.words('english'))

punctuation = set(string.punctuation) | {'--', '``', "''", '...'}

filtered_words = [
    w.lower() for w in words 
    if w.lower() not in stop_words 
    and w not in punctuation 
    and w.isalpha()
]

print(f"Кількість слів після очищення: {len(filtered_words)}")

fdist_clean = FreqDist(filtered_words)
top_10_clean = fdist_clean.most_common(10)

print("\n10 найбільш вживаних слів (після очищення):")
print(top_10_clean)

words_clean, counts_clean = zip(*top_10_clean)

plt.figure(figsize=(12, 6))
plt.bar(words_clean, counts_clean, color='lightgreen')
plt.title("Топ-10 слів у тексті 'Persuasion' (без стоп-слів)")
plt.xlabel("Слова")
plt.ylabel("Кількість")
plt.show()