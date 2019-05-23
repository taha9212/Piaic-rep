#Table
for i in range(2,6):
    for j in range(1,11):
        print(i, '*', j, '=', i * j)
    print('-----------')
#Ascending Stars
for i in range (1,6):
    for j in range (i):
        print('*', end =" ")
    print("\n")
#Descening Stars
for i in range (1,6):
    for j in range (i,6):
        print('*', end =" ")
    print("\n")
#Diagonal
for i in range (1,6):
    for j in range (i,6):
        print("", end = " ")
    print("*")