def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_counts = {}
    for char in text:
        char = char.lower()
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_characters(char_counts):
    char_list = []
    for char, count in char_counts.items():
        char_dict = {'char': char,'count': count}
        char_list.append(char_dict)
    char_list.sort(key=lambda x: x['count'], reverse=True)
    return char_list