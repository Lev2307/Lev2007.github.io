dict_scores = {
    'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1, 'l': 1, 'n': 1, 'r': 1, 's': 1, 't': 1,
    'd': 2, 'g': 2,
    'b': 3, 'c': 3, 'm': 3, 'p': 3,
    'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4,
    'k': 5,
    'j': 8, 'x': 8,
    'q': 10, 'z': 10
}
val = list(dict_scores.values())
def scrabble_score(stg):
    str = stg.lower()
    result = 0
    for s in str:
        iteration = -1
        for n in dict_scores:
            iteration += 1 
            if s == n or s != ' ':
                result += val[iteration]
                break
    return result

assert scrabble_score("") == 0, "returns 0 for ''"
assert scrabble_score('a') == 1, 'returns 1 for a'
assert scrabble_score("street") == 6, 'returns 6 for street'
assert scrabble_score("STREET") == 6, 'returns 6 for STREET'
assert scrabble_score(' a') == 1, 'returns score of " a" (with space)'
assert scrabble_score("st re et") == 6, 'returns 6 for street with whitespaces'