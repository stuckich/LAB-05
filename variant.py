text = "Анна, армия! Я читаю. Книга, край, рама.."

raw_words = text.split()

cleaned_words = []

for word in raw_words:
    cleaned = word.strip(".,!?;:").lower()
    
    if cleaned == "":
        continue
        
    cleaned_words.append(cleaned)

if len(cleaned_words) > 0:
    for w in cleaned_words:
        print(w)
    
    print(f"Количество: {len(cleaned_words)}")
else:
    print("Нет совпадений")
    print("Количество 0")
