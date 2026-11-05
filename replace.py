text = input("Введите текст: ")

colon_count = text.count(":")

modified_text = text.replace(":", "-")

print(f"Количество замен: {colon_count}")
print(f"Новый текст: {modified_text}")
