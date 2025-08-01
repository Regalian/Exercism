import re

def translate(text: str) -> str:
    """Translate a text into Pig Latin.

    Rules:
    1. If the word starts with a vowel or 'xr' or 'yt', add 'ay' to the end.
    2. If the word starts with one or more consonants move the consonants to the end and add 'ay'.
    3. If the word starts with zerp or more consonants followed by 'qu', move the consonants  (if any) and the 'qu' to the end and add 'ay'.
    4. If the word starts with one or more consonants followed by 'y', move the consonants preceding the 'y'to the end and add 'ay'.

    param: text: str Text to be translated into Pig Latin.
    returns: str Translated text in Pig Latin.
    """

    words = text.split(' ')

    translated = []
    for word in words:
        # Rule 1: Check if the text starts with a vowel or 'xr' or 'yt'
        if word.startswith(('a', 'e', 'i', 'o', 'u', 'xr', 'yt')):
            translated  += [word + 'ay']
        # Rule 2: Check if the text starts with one or more consonants followed by 'qu'
        elif match := re.match(r'^([bcdfghjklmnpqrstvwxyz]+)(.*)', word):
            # Rule 3: Check if the text starts with zerp or more consonants followed by 'qu'
            if match2 := re.match(r'^([bcdfghjklmnpqrstvwxyz]*qu)(.*)', word):
                translated += [match2.group(2) + match2.group(1) + 'ay']
            # Rule 4: Check if text starts with one or more consonants followed by 'y'
            elif match2 := re.match(r'^([bcdfghjklmnpqrstvwxyz]+)y(.*)', word):
                translated += ['y' + match2.group(2) + match2.group(1) + 'ay']
            # Rule 2
            else:
                translated += [match.group(2) + match.group(1) + 'ay']
    return ' '.join(translated)
