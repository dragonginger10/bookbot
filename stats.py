def get_num_words(text:str) -> int:
    return len(text.split())

def get_num_chars(text:str) -> dict[str, int]:
    char_count = {}
    for char in text:
        # if not char.isalpha():
        #     continue
        if char.lower() in char_count:
            char_count[char.lower()] += 1
        else:
            char_count[char.lower()] = 1

    return char_count
