def build_template(g):
    for i in range(g):
      print(str(i + 1) * (i + 1))

user_input = int(input('Введите число: '))

def main():
    build_template(user_input)

main()