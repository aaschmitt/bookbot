from stats import get_char_count_dict, get_word_count, format_dicts
import sys


def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
        return file_contents


def validate_input(args):
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


def main():
    validate_input(sys.argv)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    char_count_map = get_char_count_dict(book_text)
    char_count_list = format_dicts(char_count_map)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(book_text)} total words")
    print("--------- Character Count -------")

    for entry in char_count_list:
        print(f"{entry['char']}: {entry['num']}")

    print("============= END ===============")


main()
