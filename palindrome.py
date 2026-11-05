text = input("Введите текст для проверки: ")

cleaned_text = text.lower().replace(" ", "")

if not cleaned_text:
    print("Нет текста")
else:
    is_palindrome_slice = cleaned_text == cleaned_text[::-1]
    
    is_palindrome_loop = True
    length = len(cleaned_text)
    for i in range(length // 2):
        if cleaned_text[i] != cleaned_text[length - 1 - i]:
            is_palindrome_loop = False
            break
            
    if is_palindrome_slice:
        print("Палиндром")
    else:
        print("Не палиндром")
