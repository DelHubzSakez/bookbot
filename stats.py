def get_num_words(text):
    split_text = text.split()
    return len(split_text)

def get_num_char(text):
    char_count = {}
    no_dup = text.lower()
    for c in no_dup:
        if c in char_count:
           char_count[c] = char_count[c] + 1
        else:
            char_count[c] = 1
    return char_count

def list_dict(char_count):
    dict_list = []
    for p in char_count:
        dict_list.append({"char" : p , "num" : char_count[p]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list  

def sort_on(char_count):
    return char_count["num"]
