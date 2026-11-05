text = input("Введите исходный текст: ")

words = text.split()
normalized_text = " ".join(words)
word_count = len(words)

print(f"Исходный текст: {text}")
print(f"Нормализованный текст: {normalized_text}")
print(f"Количество слов: {word_count}")
