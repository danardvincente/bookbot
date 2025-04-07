

def get_numberof_words(content):
    the_words = content.split()

    return len(the_words)


def get_number_of_a_character(content):
    char_count = {}

    for char in content.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count