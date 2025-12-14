def get_num_words(path_to_file):
    with open(path_to_file, encoding="utf-8") as f:
        file_contents = f.read()
        words = file_contents.split()
        num_words = len(words)
    return num_words

def get_book_text(path_to_file):
    with open(path_to_file, encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents

def count_book_char(file_contents):
    char_count_dict = {}
    all_char_lowered = file_contents.lower()
    for char_num in all_char_lowered:
            if char_num in char_count_dict:
                char_count_dict[char_num] += 1
            else:
                char_count_dict[char_num] = 1
    return char_count_dict

def pair_char_and_count(char_count_dict):
    list_of_char_num_dicts = []
    for char, num in char_count_dict.items():
        list_of_char_num_dicts.append({"char": char, "num": num})
    return list_of_char_num_dicts

def get_num(list_of_char_num_dicts):
    return list_of_char_num_dicts["num"]

