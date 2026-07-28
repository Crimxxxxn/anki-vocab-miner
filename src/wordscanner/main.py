from sudachipy import Dictionary
import requests

def readText(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            return text
    except FileNotFoundError:
        print("File not found")


"""
Sets the words that are allowed, as we don't want to show unnecessary particles, grammar etc
Allows nouns, verbs, adjectives and adverbs
"""
allowedWords = {"名詞", "動詞", "形容詞", "副詞"} #{"noun, verb, adjective, adverb"}

tokenizer = Dictionary().create()

defaultPath = input("Enter file path: ") #User inputs directory of the desired text file to mine
fileToRead = defaultPath.replace('\\', '/') #Backslashes are replaced with forward slashes as they create issues

text = readText(fileToRead)

tokens = tokenizer.tokenize(text)

wordsExtracted = set()

#Adds words in dictionary form to the set, as long as they meet the criteria of allowedWords
for token in tokens:
    wordType = token.part_of_speech()

    if wordType[0] in allowedWords:
        wordsExtracted.add(token.dictionary_form())
print(wordsExtracted)


newWords = set()

for word in wordsExtracted:
    payload = {
        "action": "findNotes",
        "version": 6,
        "params": {
            # Searches for the word within the Kaishi deck
            "query": f'deck:"Kaishi 1.5k" {word}' 
        }
    }

    response = requests.post("http://localhost:8765", json=payload).json()
    note_ids = response.get("result", [])

    if note_ids:
        continue
    else:
        print(f"'{word}' is NEW (not found in deck).")
        newWords.add(word)


output_file = "new_words.txt"

# Write each unique word to a line in the text file
with open(output_file, "w", encoding="utf-8") as f:
    for word in newWords:
        f.write(f"{word}\n")

print(f"Successfully saved {len(newWords)} new words to {output_file}!")