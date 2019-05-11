print ("Mark sheet")
print ("Choose your Education level")
print ("1. SSC part I or II\n2. HSC part I or II")
choice = int ( input ("\nChoice: "))

if not (choice == 1 or choice == 2):
    print ("wrong Choice")
elif (choice == 1):
    print ("Choose Class: ")
    print ("1. 9th \n2. 10th")
    classc = int (input ("\nChoice: "))
    if not (classc == 1 or classc == 2):
        print ("\nwrong choice")
    elif classc == 1:
        print ("Enter 9th class subjects, Total marks and Obtained Marks ")
        sub1 = input ("\nEnter your 1st subject: ")
        total_marks1 = int (input ("Total Marks of 1st Subject: "))
        obtain_marks1 = float (input ("Obtain Marks of the 1st Subject "))
        sub2 = input ("\nEnter your 2nd subject: ")
        total_marks2 = int (input ("Total Marks of 2nd Subject: "))
        obtain_marks2 = float (input ("Obtain Marks of the 2nd Subject "))
        sub3 = input ("\nEnter your 3rd subject: ")
        total_marks3 = int (input ("Total Marks of 3rd Subject: "))
        obtain_marks3 = float (input ("Obtain Marks of the 3rd Subject "))
        sub4 = input ("\nEnter your 4th subject: ")
        total_marks4 = int (input ("Total Marks of 4th Subject: "))
        obtain_marks4 = float (input ("Obtain Marks of the 4th Subject "))
        sub5 = input ("\nEnter your 5th subject: ")
        total_marks5 = int (input ("Total Marks of 5th Subject: "))
        obtain_marks5 = float (input ("Obtain Marks of the 5th Subject "))
    else :
        print ("Enter 10th class subjects, Total marks and Obtained Marks ")
        sub1 = input ("\nEnter your 1st subject: ")
        total_marks1 = int (input ("Total Marks of 1st Subject: "))
        obtain_marks1 = float (input ("Obtain Marks of the 1st Subject "))
        sub2 = input ("\nEnter your 2nd subject: ")
        total_marks2 = int (input ("Total Marks of 2nd Subject: "))
        obtain_marks2 = float (input ("Obtain Marks of the 2nd Subject "))
        sub3 = input ("\nEnter your 3rd subject: ")
        total_marks3 = int (input ("Total Marks of 3rd Subject: "))
        obtain_marks3 = float (input ("Obtain Marks of the 3rd Subject "))
        sub4 = input ("\nEnter your 4th subject: ")
        total_marks4 = int (input ("Total Marks of 4th Subject: "))
        obtain_marks4 = float (input ("Obtain Marks of the 4th Subject "))
        sub5 = input ("\nEnter your 5th subject: ")
        total_marks5 = int (input ("Total Marks of 5th Subject: "))
        obtain_marks5 = float (input ("Obtain Marks of the 5th Subject "))
else:
    print ("Choose Class ")
    print ("1. 1st Year\n2. 2nd Year")
    classc = int (input ("/nChoice: "))
    if not(classc == 1 or classc == 2):
        print ("\nWorng Choice")
    elif classc == 1:
        print ("Enter 1st Year subjects, Total marks and Obtained Marks ")
        sub1 = input ("\nEnter your 1st subject: ")
        total_marks1 = int (input ("Total Marks of 1st Subject: "))
        obtain_marks1 = float (input ("Obtain Marks of the 1st Subject "))
        sub2 = input ("\nEnter your 2nd subject: ")
        total_marks2 = int (input ("Total Marks of 2nd Subject: "))
        obtain_marks2 = float (input ("Obtain Marks of the 2nd Subject "))
        sub3 = input ("\nEnter your 3rd subject: ")
        total_marks3 = int (input ("Total Marks of 3rd Subject: "))
        obtain_marks3 = float (input ("Obtain Marks of the 3rd Subject "))
        sub4 = input ("\nEnter your 4th subject: ")
        total_marks4 = int (input ("Total Marks of 4th Subject: "))
        obtain_marks4 = float (input ("Obtain Marks of the 4th Subject "))
        sub5 = input ("\nEnter your 5th subject: ")
        total_marks5 = int (input ("Total Marks of 5th Subject: "))
        obtain_marks5 = float (input ("Obtain Marks of the 5th Subject "))
        sub6 = input ("\nEnter your 6th subject: ")
        total_marks6 = int (input ("Total Marks of 6th Subject: "))
        obtain_marks6 = float (input ("Obtain Marks of the 6th Subject "))
    else :
        print ("Enter 2nd year subjects, Total marks and Obtained Marks ")
        sub1 = input ("\nEnter your 1st subject: ")
        total_marks1 = int (input ("Total Marks of 1st Subject: "))
        obtain_marks1 = float (input ("Obtain Marks of the 1st Subject "))
        sub2 = input ("\nEnter your 2nd subject: ")
        total_marks2 = int (input ("Total Marks of 2nd Subject: "))
        obtain_marks2 = float (input ("Obtain Marks of the 2nd Subject "))
        sub3 = input ("\nEnter your 3rd subject: ")
        total_marks3 = int (input ("Total Marks of 3rd Subject: "))
        obtain_marks3 = float (input ("Obtain Marks of the 3rd Subject "))
        sub4 = input ("\nEnter your 4th subject: ")
        total_marks4 = int (input ("Total Marks of 4th Subject: "))
        obtain_marks4 = float (input ("Obtain Marks of the 4th Subject "))
        sub5 = input ("\nEnter your 5th subject: ")
        total_marks5 = int (input ("Total Marks of 5th Subject: "))
        obtain_marks5 = float (input ("Obtain Marks of the 5th Subject "))
        sub6 = input ("\nEnter your 6th subject: ")
        total_marks6 = int (input ("Total Marks of 6th Subject: "))
        obtain_marks6 = float (input ("Obtain Marks of the 6th Subject "))
if choice == 1:
    print ("Your SSC Marks Sheet")
    print ("\nSubject             Total Marks             Obtain Marks")
    print (sub1,"               ",total_marks1,"                ",obtain_marks1)
    print (sub2,"               ",total_marks2,"                ",obtain_marks2)
    print (sub3,"               ",total_marks3,"                ",obtain_marks3)
    print (sub4,"               ",total_marks4,"                ",obtain_marks4)
    print (sub5,"               ",total_marks5,"                ",obtain_marks5)
    percentage = ((obtain_marks1 + obtain_marks2 + obtain_marks3 + obtain_marks4 + obtain_marks5)/(total_marks1 + total_marks2 + total_marks3 + total_marks4 + total_marks5))*100
    print ("\nYour Percentage is ", percentage ,"%")
    if percentage <= 39 and percentage >= 35 :
        print ("E Grade ") 
    elif percentage <= 49 :
        print ("D Grade ")
    elif percentage <= 59 :
        print ("C Grade ")
    elif percentage <= 69 :
        print ("B Grade ")
    elif percentage <= 79 :
        print ("A Grade ")
    elif percentage >= 80 :
        print ("A+ Grade ")
    else :
        print("Fail :p ")
else :
    print ("Your HSC Marks Sheet")
    print ("\nSubject             Total Marks             Obtain Marks")
    print (sub1,"               ",total_marks1,"                ",obtain_marks1)
    print (sub2,"               ",total_marks2,"                ",obtain_marks2)
    print (sub3,"               ",total_marks3,"                ",obtain_marks3)
    print (sub4,"               ",total_marks4,"                ",obtain_marks4)
    print (sub5,"               ",total_marks5,"                ",obtain_marks5)
    print (sub6,"               ",total_marks6,"                ",obtain_marks6)
    percentage = ((obtain_marks1 + obtain_marks2 + obtain_marks3 + obtain_marks4 + obtain_marks5 + obtain_marks6)/(total_marks1 + total_marks2 + total_marks3 + total_marks4 + total_marks5 + total_marks6))*100
    print ("\nYour Percentage is ", percentage ,"%")
    if percentage <= 39 and percentage >= 35 :
        print ("E Grade ") 
    elif percentage <= 49 :
        print ("D Grade ")
    elif percentage <= 59 :
        print ("C Grade ")
    elif percentage <= 69 :
        print ("B Grade ")
    elif percentage <= 79 :
        print ("A Grade ")
    elif percentage >= 80 :
        print ("A+ Grade ")
    else :
        print("Fail :p ")