def build_template_input():
        """
        output: return str, built-in input() function
        """
        return input('Введите размер поля: ')
def build_template(w):
        """
        input: w - string (word)
        output: replace all chars in string to '_',
        return replaced chars as string with length w == tmp
        """
        tmp = []
        for l in w:
            tmp.append('_')
        return tmp

def game():
    gameStatus = True

    size_of_template = build_template_input()
    template = build_template(size_of_template)

game()