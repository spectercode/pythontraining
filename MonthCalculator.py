#State name function of code.
print ("Month Calculator")

#Add a statement to inform user of what to do.
print ("Input a number between 1 and 12 for the current month")

#The input below will wait for a numeral from the executor.
month = int(input ("Please choose a number: "))

#Variables set as the different months to be called.
m1 = "January"
m2 = "February"
m3 = "March"
m4 = "April"
m5 = "May"
m6 = "June"
m7 = "July"
m8 = "August"
m9 = "September"
m10 = "October"
m11 = "November"
m12 = "December"

#If and else statements to print based on input.
if month == 1:
    print(m1)
elif month == 2:
    print(m2)
elif month == 3:
    print(m3)
elif month == 4:
    print(m4)
elif month == 5:
    print(m5)
elif month == 6:
    print(m6)
elif month == 7:
    print(m7)
elif month == 8:
    print(m8)
elif month == 9:
    print(m9)
elif month == 10:
    print(m10)
elif month == 11:
    print(11)
elif month == 12:
    print(12)

else:
    print ('Please specify a number between 1-12')

#Alternative way of doing see below.
# elif month == 1:
#   print("January")