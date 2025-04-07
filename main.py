from stats import get_numberof_words, get_number_of_a_character


def get_book_text(file_path):

    with open(file_path, "r") as bk_file:
        bk_contents = bk_file.read()

    return bk_contents
    


def main():
    book_file = "./books/frankenstein.txt"
    frank_bk_contents = get_book_text(book_file)

    # print(frank_bk_contents)
    num_words = get_numberof_words(frank_bk_contents)
    print(f"{num_words} words found in the document")

    num_char = get_number_of_a_character(frank_bk_contents)

    for char, amt in num_char.items():
        print(f"'{char}': {amt}")



main()