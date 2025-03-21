from stats import (get_num_words,
count_char,
sort_on,
organize_data
)
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    book = sys.argv[1]

def main():
    book_path = book
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = count_char(text)
    new_list = organize_data(num_chars)

    # Sort the list by count
    new_list.sort(reverse=True, key=sort_on)
    
    # Printing for readability
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    # Loop through the list to print to each line
    for chars in new_list:
        char = chars['char']
        count = chars['count']
        if char.isalpha():    # Alphabetical characters only
            print(f"{char}: {count}")
    print("============= END ===============")

# Reads the book
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()