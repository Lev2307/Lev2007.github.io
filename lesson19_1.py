first_dict = {'a' : 1, 'e' : 2, 'i' : 3, 'o' : 4, 'u' : 5}
second_dict = {'1' : 'a', '2' : 'e', '3' : 'i', '4' : 'o', '5' : 'u'}

def encode(st):
    variable = ''
    for i in st:
        if i in first_dict:         
            variable += str(first_dict[i])
        else:            
            variable += i
    return variable
    
def decode(st):   
    variable = ''
    for i in st:
        if i in second_dict:          
            variable += str(second_dict[i])
        else:
            variable += i
    return variable
    
assert encode('hello') == 'h2ll4', 'Test failed'
assert encode('How are you today?') == 'H4w 1r2 y45 t4d1y?', 'Test failed'
assert encode('This is an encoding test.') == 'Th3s 3s 1n 2nc4d3ng t2st.', 'Test failed'
assert decode('h2ll4') == 'hello', 'Test failed'