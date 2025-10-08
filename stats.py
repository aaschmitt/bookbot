def get_word_count(text):
    return len(text.split())


def get_char_count_dict(text):
    res = {}
    for char in text:
        char = char.lower()
        if char in res:
            res[char] += 1
            continue
        res[char] = 1
    return res


def sort_on(items):
    return items["num"]


def format_dicts(char_count_dict):
    res = []
    for key in char_count_dict.keys():
        if not key.isalpha():
            continue

        res.append({
            "char": key,
            "num": char_count_dict[key]
        })

    res.sort(key=sort_on, reverse=True)

    return res
