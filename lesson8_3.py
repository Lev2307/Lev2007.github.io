def draw_template(r):
    for i in range(r):
        print(str(i + 1) * (i + 1))

def user_input():
  return int(input('ведите число: '))

def main():
    number = user_input()
    draw_template(number)

main()
