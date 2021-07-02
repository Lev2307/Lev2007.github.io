def pallindrom(string):
    return string == string[::-1]

def funv(string, number):
    tmp = []
    result = False
    for i in range(len(string)):
        tmp.append(string[i])
        if len(tmp) == number:
            result = pallindrom(tmp)
        elif len(tmp) > number:
            tmp.pop(0)
            result = pallindrom(tmp)
        if result:
            print(tmp)
            return tmp

funv('hello', 2)