print ("Finding Prime Number")
p_num = int ( input ( "Enter any number: "))
for i in range(2,p_num):
    if p_num % i == 0:
        print("The given number is not a prime number")
        break
    else:
        print("The given number is a prime number")
        break