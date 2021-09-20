#'''''''''''''''''''''''''''''''''''''''''''''''''
a = int(input("first number:"))
b = int(input("second number:"))
c = int(input("third number:"))
sum = a + b + c
print("sum of three numbers=", sum)
print(f"sum of three numbers is {sum}")
print("sum of three numbers is {}".format(sum))

#''''''''''''''''''''''''''''''''''''''''''''''''''
# Taking multiple inputs in one statement
x, y = input("enter numbers:").split()
print("multiplication of x and y is", x * y)

x = list(map(int, input("enter number:").split()))
print("list of students:", x)
#'''''''''''''''''''''''''''''''''''''''''''''''''''

#3.	Write a Python program to find total bill of a restaurant,
# take bill amount and tax percent from user and
# then display the total bill

def total_bill(bill, tax):
    final_bill = bill + bill * (tax/100)
    print("final bill with tax: Rs", final_bill, "/-")

a = total_bill(50, 25)
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Write a program to swap 2 numbers in two variables
x = 10
y = 20
(x, y) = (y, x)
print(x, y)
