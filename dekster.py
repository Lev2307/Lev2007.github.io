def make_dict(string):
    tmp = 1
    dictionary = {}
    for i in string:
        if not i in dictionary:
            dictionary[i] = tmp
        else:
            dictionary[i] += tmp
    print(dictionary)
    return dictionary

make_dict('hello')

def find_unic_letter(string):
    tmp = 1
    dictionary = {}
    for i in string:
        if not i in dictionary:
            dictionary[i] = tmp
        else:
            dictionary[i] += tmp
    for j in string:
        if dictionary[j] == tmp:
            return j
    print(dictionary)
    return dictionary

print(find_unic_letter('ohellehoz'))