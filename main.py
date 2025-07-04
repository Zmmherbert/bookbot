from stats import count_words
from stats import char_count
import sys

def get_book_text(filepath):
    with open(filepath) as book:
        return book.read()
    
def sort_on(items):
    return items["num"]

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    book = get_book_text(filepath)
    # print(get_book_text("books/frankenstein.txt"))

    word_count = count_words(book)
    # print(f"{word_count} words found in the document")

    char_frequency = char_count(book)
    # print(char_frequency)
    
    print(f"""============ BOOKBOT ============
Analyzing book found at {filepath}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------""")
    
    frequency_list = []
    for char in char_frequency:
        frequency_list.append({"character": char, "num": char_frequency[char]})
    frequency_list.sort(reverse=True, key=sort_on)
    for entry in frequency_list:
        if (entry["character"].isalpha()):
            print(f"{entry["character"]}: {entry["num"]}")
    print("============= END ===============")

    

main()