print ("My simple calculator ")
print ("1. Add")
print ("2. Subtract")
print ("3. Divide")
print ("4. Multiply")
# this below can be user, select, anything that makes sense to
user = int(input ("Please choose an Operation "))

n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the second number: '))

if user == 1:
    print (n1 + n2)
elif user == 2:
    print(n1 - n2)
elif user == 3:
    print(n1 // n2)
elif user == 4:
    print(n1 * n2)