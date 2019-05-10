print ("9th class Mark Sheet")
marks_sindhi = float(input("Enter your Sindhi Marks: "))
marks_cb = float(input("Enter your Computer / Biologoy Marks: "))
marks_english = float(input("Enter your English Marks: "))
marks_pak = float(input("Enter your Pakistan Studies Marks: "))
marks_chem = float(input("Enter your Chemistry Marks: "))
percentage = ((marks_cb + marks_chem + marks_english + marks_pak + marks_sindhi)/425)*100
print("*******************")
print ("Your percentage: ", percentage) 

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
print("*******************")