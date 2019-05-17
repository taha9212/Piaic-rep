import random
temp = 0
array = []
for i in range (50):
    array.append(random.randint(0,50))
print (array)
for i in range(50):
    if array[0] > array[i]:
        temp = array [0]
        array[0] = array [i]
        array[i] = temp
print("smallest number is :" , array[0])
