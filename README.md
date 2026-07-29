## Anki vocab miner
This is a tool I made to help me batch mine words that I don't know (that aren't in my anki deck) from Japanese media (like books, VN text, anime subtitles etc), but I am releasing it for anyone to use. It scans a text file and creates a new one (new_words.txt) with words that aren't found in the deck, all in dictionary form. Intended use is for the user to obtain a text file version of whatever it is they wish to mine, use this tool, and then open the file generated in a browser. This will mean that they can use browser extensions such as yomitan popup dictionary to create their flashcards easily, and can do what the batch mining feature of Migaku does but for free.

## How to use
1. Locate the text file you want to scan and copy its file path, e.g "C:\JapaneseMedia\mytext.txt"
2. Ensure that you have anki open
3. Run the tool
4. Copy the file path when prompted
5. Enter the name of the anki deck you want to scan, e.g "Kaishi 1.5"
6. Once the program is finished, go to "new_words.txt" and open it in your browser
7. You can then use your browser extensions if you have them enabled, and can mine the words quickly as you have a list of them

## Prerequisites
*Python 3.8 or higher
*Anki
*AnkiConnect addon installed on Anki
*[SudachiPy](https://github.com/WorksApplications/SudachiPy)
*[requests](https://requests.readthedocs.io/)

## License
This project is licensed under the MIT license. See the LICENSE file for details.
