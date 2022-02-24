#print (4> 2)
#print (1>3)
#print (10 != 100)
#print (10 != 10)
#print ("hello" == "hello")
#print ("hello" != "world")
#print (4>1 and "word" == "word")

#veg = input("type the name of a vegetable ")

#if veg == "corn":
    #print("the vegetable is corn.")
#else:
    #print("The vegetable is not corn.")

Loan = input("Are you applying for a loan? ")
if Loan == "yes":
    gpa = float(input ("what is your highschool GPA? "))
else:
     print ("Goodbye")
     quit()

if gpa >= 3.7:
    acc = input("Is the loan accepted? ")
    if acc == "yes":
            print("CONGRATULATIONS! You qualify for a low APR loan!")
    else:
        print("SORRY, your loan has not been accepted by the approved institution")

else:
  print("You need a higher GPA (at least 3.7) to qualify :( , Goodbye.")