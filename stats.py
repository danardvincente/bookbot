

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


def sort_character(char_dict):
    """ sorts the char_dict by amount of words in desc order. """
    char_amt_desc = {s_char:s_amt for s_char, s_amt in sorted(char_dict.items(), key=lambda item: item[1], reverse=True)}

    return char_amt_desc

