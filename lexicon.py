
lexicon = {
    "north": 'direction',
    "south": 'direction',
    "east": 'direction',
    "go": 'verb',
    "kill": 'verb',
    "eat": 'verb',
    "the": 'stop',
    "in": 'stop',
    "of": 'stop',
    "bear": 'noun',
    "princess": 'noun',
    "ASDFADFASDF": 'error',
    "IAS": 'error'
}

def scan(sentence):
    pass
    result = []
    """ sentence got its value from scan('input').
        Then it splits it up in parts and will be values 
        for word in the loop.
        For each loop word compare its value(part) 
        to the content in lexicon."""
    sentence = sentence.split()
    for word in sentence:
        wordtype = lexicon.get(word, 'error')
        pair = (wordtype, word)

        """If there is a match it will append the wordtype + word to result. """
        if word in lexicon: #1
            result.append(pair)

            """ Then it look if it is a number(str). 
            If so it convert it with function convert_int to a integer. 
            Then pair adds 'number + the integer to a."""
        elif word not in lexicon: 
            number = convert_number(word)
            if number:
                pair = ('number', number)

                """If neither of the two previous condition is met, 
                it sets pair to wordtype with its default value (error)"""
            elif word not in lexicon and not number:
                pair = (wordtype, word)
            result.append(pair)

    return result

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None