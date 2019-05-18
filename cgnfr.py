import random
temp = 0
print ('Find greater number from random number')
array = []
for i in range(50) :
    array.append( random.randint(1,200))
print (array)
for i in range(50):
    if array[0] < array [i]:
        temp = array[0]
        array [0] = array[i]
        array [i] = temp
print ("larget number is : ", array [0])
summ = sum(array)
print("Sum of numbers are: ", summ)
mean  = summ / len(array)
print ("Mean  = ", mean)