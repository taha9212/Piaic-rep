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
#Diamond
n = 5
for i in range (0,n):
    for j in range (0,n):
        print(" ", end = " ")
    for k in range (0,(i*2-1)):
        print("*", end = " ")
    print("")
    n -= 1
m = 5
for i in range (0,m):
    for j in range (0,i):
        print(" ", end = " ")
    for k in range (0, m*2-1):
        print("*", end = " ")
    print("")
    m-=1