from lab_4.main import LetterStorage, tokenize_by_letters


with open('reference_text.txt', encoding='utf-8') as file:
    text = file.read()

tokenized = tokenize_by_letters(text)
storage = LetterStorage()
storage.update(tokenized)

print('The number of letters in the storage:', storage.get_letter_count())
print('Top-5 letters with the lowest id:', list(storage.storage.keys())[-5:])
print('Top-5 letters with the highest id:', list(storage.storage.keys())[:5])
