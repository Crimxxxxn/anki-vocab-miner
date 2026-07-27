#function that reads the text file in utf-8 and returns the text as string, takes file path as input
def readText(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            return text
    except FileNotFoundError:
        print("File not found")