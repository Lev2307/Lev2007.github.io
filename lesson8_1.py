sentence ='Fair is foul, and foul is fair: Hover through the fog and filthy air.'
alfabet = 'qwertyuiopasdfghjklzxcvbnm'

def lower(w):
    count = 0
    for i in w:
        for a in alfabet.lower():
            if i == a:
                count += 1
    return count

def upper(w):
    count = 0
    for i in w:
        for a in alfabet.upper():
            if i == a:
                count += 1
    return count


print(f'Total uppercase letters in sentence is: {upper(sentence)}')
print(f'Total lowercase letters in sentence is: {lower(sentence)}')