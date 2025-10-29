sentence = input("Введіть речення: ")

words = sentence.split()   

print("Слова, відмінні від 'привіт':")
for word in words:
    if word.lower() != "привіт":
        print(word)
