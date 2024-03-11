from PyDictionary import PyDictionary

dictionary = PyDictionary()

while True:
    word = input("Enter a word: ")
    if word == "":
        break
    print(dictionary.meaning(word))