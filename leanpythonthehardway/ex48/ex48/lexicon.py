directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
verbs = ['go', 'stop', 'kill', 'eat']
stops = ['the', 'in', 'of', 'from', 'at', 'it']
nouns = ['door', 'bear', 'princess', 'cabinet']

def scan(sentence):
    words = sentence.split()
    results = []
    for w in words:
        if w in directions:
            results.append(('direction', w))
            continue
        elif w in verbs:
            results.append(('verb', w))
            continue
        elif w in stops:
            results.append(('stop', w))
            continue
        elif w in nouns:
            results.append(('noun', w))
            continue

        try:
            results.append(('number', int(w)))
        except:
            results.append(('error', w))

    return results
