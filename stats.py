def count_words(text):
    return len(text.split())

def char_count(text):
    char_frequency = {}
    for char in text:
        char = char.lower()
        if char not in char_frequency:
            char_frequency[char] = 1
        else:
            char_frequency[char] += 1
    # print(char_frequency)
    return char_frequency
