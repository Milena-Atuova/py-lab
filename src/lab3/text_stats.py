import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from lib.text import normalize, tokenize, count_freq, top_n

text = sys.stdin.readline()

normalized_text = normalize(text)

tokens = tokenize(normalized_text)

total_words = len(tokens)
freq_dict = count_freq(tokens)
unique_words = len(freq_dict)
top_words = top_n(freq_dict, 5)

print(f"Всего слов: {total_words}")
print(f"Уникальных слов: {unique_words}")
print("Топ-5:")

for word, count in top_words:
    print(f"{word}:{count}")

# Таблица
USE_TABLE = True 

if USE_TABLE and top_words:
    # Вычисляем ширину первого столбца по длине самого длинного слова
    max_word_len = max(len(word) for word, i in top_words)
    header_word = "слово"
    header_freq = "частота"

    # Выровненные заголовки
    print(f"{header_word:<{max_word_len}} | {header_freq}")
    print("-" * (max_word_len + 3 + len(header_freq)))

    # Выровненные строки
    for word, count in top_words:
        print(f"{word:<{max_word_len}} | {count}")
else:
    for word, count in top_words:
        print(f"{word}:{count}")


