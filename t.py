f = open("t.txt", "w+")

f.write('1 \n')
f.write('2')

f.close()

f = open("t.txt", "a")

f.write('3 \n')
f.write('4')

f.close()
