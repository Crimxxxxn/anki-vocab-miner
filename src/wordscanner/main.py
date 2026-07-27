from readwrite import readText
from sudachipy import Dictionary

tokenizer = Dictionary().create()

defaultPath = input("Enter file path: ")
fileToRead = defaultPath.replace('\\', '/')

text = readText(fileToRead)

tokens = tokenizer.tokenize(text)

for token in tokens:
    print(token.surface(), token.dictionary_form(), token.part_of_speech())