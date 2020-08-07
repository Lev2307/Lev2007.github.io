#cписал, потому что ничего кроме списывания не умею
alfabet = 'qwertyuiopasdfghjklzxcvbnm'

def count_upper(w):
    count = 0
    for l in w:
        for a in alfabet.upper():
            if l == a:
             count += 1
    return count

def count_lower(w):
    count = 0
    for l in w:
        for a in alfabet.lower():
            if l == a:
             count += 1
    return count

sentence = 'Fair is foul, and foul is fair: Hover through the fog and filthy air.'

print(f'Total uppercase letters in sentence is: {count_upper(sentence)}')
print(f'Total lower letters in sentence is: {count_lower(sentence)}')
