import sys
from stats import get_num_words
from stats import get_num_chars
from stats import sort_dict

def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()


def main():
    print("Usage: python3 main.py <path_to_book>")
    if len(sys.argv) < 2:
        sys.exit(1)
    book = sys.argv[1]
    text = get_book_text(book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    num_words = get_num_words(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    chars_dict = get_num_chars(text)
    sorted_dict = sort_dict(chars_dict)
    print("----------- Char Count ----------")
    for hash in sorted_dict:
        print(f"{hash['char']}: {hash['num']}")

main()