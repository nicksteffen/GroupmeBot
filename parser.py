import re

def contains_key_phrase(phrase):
    word_list=[]
    word_list=phrase.split()
    for word in word_list:
        word= re.sub(r'\W+','',word)
        if word.endswith("er"):
            return word
    return False


def format_message(phrase):
    word=contains_key_phrase(phrase)
    if word == False:
        return False
    message = word[:1].upper()+word[1:-2]+" her?"
    return message
