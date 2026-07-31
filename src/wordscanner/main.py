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

filePathInput = input("Enter file path of text file: ") #User inputs directory of the desired text file to mine
fileToRead = filePathInput.replace('\\', '/') #Backslashes are replaced with forward slashes as they create issues

text = readText(fileToRead)

tokens = tokenizer.tokenize(text) #tokenizer to separate words

wordsExtracted = set()

#Adds words in dictionary form to the set, as long as they meet the criteria of allowedWords
for token in tokens:
    wordType = token.part_of_speech()

    if wordType[0] in allowedWords:
        wordsExtracted.add(token.dictionary_form())
print("found:" , wordsExtracted)


newWords = set()

deckToScan = input("Ensure that anki is running\nInput name of deck to scan: ")

payload = {
        "action": "findNotes",
        "version": 6,
        "params": {
            "query": f'deck:"{deckToScan}"' 
        }
    }

response = requests.post("http://localhost:8765", json=payload).json()
note_ids = response.get("result", [])

payload = {
    "action": "notesInfo",
    "version": 6,
    "params": {
        "notes": note_ids
    }
}

response = requests.post("http://localhost:8765", json=payload).json()
notes = response["result"]


wordFieldName = input("Input the name of the word field to scan for your deck (e.g 'Word'): ")

existing_words = set()

for note in notes:
    existing_words.add(note["fields"][f"{wordFieldName}"]["value"])

newWords = wordsExtracted - existing_words

for word in wordsExtracted:
    if word in existing_words:
        print(f"'{word}' is already in deck")
    else:
        print(f"'{word}' is not in deck")

print("new words:" , newWords)

"""
for word in wordsExtracted:
    payload = {
        "action": "findNotes",
        "version": 6,
        "params": {
            "query": f'deck:"{deckToScan}" {word}' 
        }
    }

    response = requests.post("http://localhost:8765", json=payload).json()
    note_ids = response.get("result", [])

    if note_ids:
        ##print(f"'{word} is already in deck")
        continue
    else:
        ##print(f"'{word}' is not in deck")
        newWords.add(word)
"""

output_file = "new_words.txt"

# Write each unique word to a line in the text file
with open(output_file, "w", encoding="utf-8") as f:
    for word in newWords:
        f.write(f"{word}\n")