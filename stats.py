# Counts the # of words
def get_num_words(text):
    words = text.split()
    return len(words)

# Counts the # of characters
def count_char(text):
    my_dict = {}
    letter_list = list(text.lower())
    for i in letter_list:
        if i in my_dict:
            my_dict[i] += 1
        elif i not in my_dict:
            my_dict[i] = 1
    return my_dict

# Creates a list of individual dictionaries to reference
def organize_data(count):
    result = []
    for char, count in count.items():
        char_dict = {'char': char, 'count': count}
        result.append(char_dict)
    return result

# Sort priority on the "new" list/dictionary
def sort_on(dict):
    return dict["count"]
 