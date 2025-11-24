def get_num_words(text):
    return len(text.split())

def get_num_chars(text):
    dic = { }
    for char in text.lower():
        if char == " " or char.isalpha() == False: continue

        if char not in dic:
            dic[char] = 1
        else:
            dic[char] += 1

    return dic

def sort_on(items):
    return items["num"]

def sort_dict(dic):
    new_list = []
    for k, v in dic.items():
        new_list.append({"char": k, "num": v})
    new_list.sort(reverse=True, key=sort_on)
    return new_list