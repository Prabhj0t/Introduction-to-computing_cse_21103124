# ASSIGNMENT-2
# ques1

# take input "Python is a case sensitive language"
input_string = input("Enter the string:")
# a
print("Part A:")
print("Length of string is:",len(input_string))

# b
print("Part B:")
print("reverse of string is:","'",input_string[::-1],"'")

# c
print("Part C:")
# "a case senstive" has index value 9 to 26
new_string = input_string[slice(9, 26)]
print("new string is:","'",new_string,"'")

# d
print("Part D:")
replaced_string = input_string.replace("a case sensitive", "object oriented")
print(replaced_string)

# e
print("Part E:")
print("Index of 'a' in given input string is:", input_string.index('a'))

# f
print("Part F:")
print(input_string.replace(" ", ""))

# ques2
Name = input("Enter your name:")
SID = int(input("Enter you SID:"))
DEPARTMENT = input("Enter your department:")
CGPA = float(input("Enter your CGPA:"))
print("Hey,%s Here! \n My SID is %d \nI am from %s department and my CGPA is %.2f" %
      (Name, SID, DEPARTMENT, CGPA))

# ques3
# given a=56 and b=10 using bitwise operators
a = 56
b = 10
print("a=56\nb=10")
print("Part A:")
print("a&b: ", a & b)
print("Part B:")
print("a|b: ", a | b)
print("Part C:")
print("a^b: ", a ^ b)
print("Part D:")
print("a<<2:", a << 2, "and b<<2", b << 2)
print("Part E:")
print("a>>2:", a >> 2, "and b>>4", b >> 4)

# ques4
# first taking the input by user of three no.s
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# applying conditional
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3

print("The largest number is", largest)

# ques5
# first taking input string by user
input_string = input("Enter the string: ")
if ("name" in input_string):
    print("Yes, 'name' is present in this string")
else:
    print("No, 'name' is not present in this string")


# ques6
# define the sides of a triangle with variable a,b and c.
side1 = int(input("Enter the value of side a:"))
side2 = int(input("Enter the value of side b:"))
side3 = int(input("Enter the value of side c:"))
# using conditional statment
# any of three side shouldn't greater than the some of other two sides
if ((side3) < ((side1)+(side2))) and ((side2) < ((side1)+(side3))) and ((side1) < ((side2)+(side3))):
    print("Yes")
else:
    print("No")

