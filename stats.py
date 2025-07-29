def number_of_words(text):
    words = text.split()
    number_words = len(words)
    return number_words

def character_count(text):
    characters = {}
    for t in text.lower():
        if t in characters:
            characters[t] += 1
        else:
            characters[t] = 1
    return characters

def sort_on(item):
    return item["num"]

def character_sort(char_dict):
    sorted_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

    
