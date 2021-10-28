import random
counter = 0
a_count = 0
b_count = 0
c_count = 0
d_count = 0
e_count = 0
f_count = 0

while counter < 10000: 
    a = random.randint(1,6)

    if a == 1:
        a_count += 1
    if a == 2:
        b_count += 1
    if a == 3:
        c_count += 1
    if a == 4:
        d_count += 1
    if a == 5:
        e_count += 1
    if a == 6:
        f_count += 1
    counter += 1
print('1 wysolowany %s razy' % (a_count))
print('2 wysolowany %s razy' % (b_count))
print('3 wysolowany %s razy' % (c_count))
print('4 wysolowany %s razy' % (d_count))
print('5 wysolowany %s razy' % (e_count))
print('6 wysolowany %s razy' % (f_count))
    
    # print(list)