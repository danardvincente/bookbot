import sys
from stats import get_numberof_words, get_number_of_a_character, sort_character


def get_book_text(file_path):

    with open(file_path, "r") as bk_file:
        bk_contents = bk_file.read()

    return bk_contents
    


def main():
    book_file = sys.argv  # returns ['main.py', '<path_to_book>']
    # uses a command-line arguement to get path to book: python3 main.py books/name_of_book.txt

    if len(book_file) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        frank_bk_contents = get_book_text(book_file[1])

        print("=============== BOOKBOT ==============")
        print(f"Analyzing book found at {book_file[1]}...")

        print("----------- Word Count -----------")
        num_words = get_numberof_words(frank_bk_contents)
        print(f"Found {num_words} total words")

        num_char = get_number_of_a_character(frank_bk_contents)

        print("----------- Character Count -----------")
        sort_chars = sort_character(num_char)
        for char, amt in sort_chars.items():
            if char.isalpha():
                print(f"{char}: {amt}")


        print("================ END =================")


main()