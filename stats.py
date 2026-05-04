def get_num_words(text):
    num_words = len(text.split())
    return num_words

def get_num_times(text):
    words = {}

    for char in text:
        lower_char = char.lower()

        if lower_char in words:
            words[lower_char] += 1
        else:
            words[lower_char] = 1
        
    return words


def sorted_list(words):
    sorted_char = []
    for word in words:
        if word.isalpha() == False:
            continue

        sorted_char.append({"char": word, "num": words[word]})
    
    def sort_on(d):
        return d["num"]
        
    sorted_char.sort(reverse=True, key=sort_on)
        
    return sorted_char


