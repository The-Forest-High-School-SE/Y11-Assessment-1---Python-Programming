import requests

# You can ignore how this function works, it's just used to get the list of words in all_words above
def get_valid_wordle_words():
    str_words = []
    words_text = requests.get("https://raw.githubusercontent.com/tabatkins/wordle-list/refs/heads/main/words") \
                        .content
    words = words_text.split()
    for word in words:
        str_words.append(str(word.decode('ascii')))
    return str_words

# all_words will contains a list of all valid words that you can use
all_words = get_valid_wordle_words()






