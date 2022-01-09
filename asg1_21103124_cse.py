#    ASSIGNMENT 1
#QUESTION 1 
# first we declare the numbers and take input from user
num1=int(input("enter the value of num1:"))
num2=int(input("enter the value of num2:"))
num3=int(input("enter the value of num3:"))
average= float((num1+num2+num3)/3)
print("the Average of three numbers you entered is :",average)


#QUESTION 2
# take input from user of their gross income 
# and no. of dependents
gross_income = int(input("Enter your Gross income: "))

Dependents = int(input("enter the number of dependents: "))

standard_deduction = 10000 #all taxpayers are allowed this standard deduction

deduction =3000 #it is the deduction per dependents

Tax_rate =0.20 # the tax rate 20%
Taxable_income = gross_income-standard_deduction-(Dependents*deduction)
Tax = float(Taxable_income*Tax_rate)
print("The Final Tax amount should be paid is: ",Tax)

#QUESTION 3
# take input from student of his/her information name,course,SID,Gender,CGPA
# and make list of it as output
SID = int(input("Enter your StudentID:"))
Name = input("enter your Name:")

Gender = input("enter your Gender M/F/U:")
if(Gender == 'M'):
 Gender = "Male"
elif(Gender == 'F'):
 Gender = "Female"
else:
 Gender = "unknown"
 
Course = input("enter your course you studing:")
CGPA = float(input("enter your CGPA:"))
# store the value from user and making list of all the information
Student = [SID, Name, Gender, Course, CGPA]
# now we printing the details
print("\n***STUDENT DETAIL***")
print(Student)

#QUESTION 4
# take the marks of five students then arrange in list then sort in and get sorted output
marks1ststudent = int(input("Marks of 1st student : "))
marks2ndstudent = int(input("Marks of 2nd student : "))
marks3rdstudent = int(input("Marks of 3rd student : "))
marks4thstudent = int(input("Marks of 4th student : "))
marks5thstudent = int(input("Marks of 5th student : "))
SortedMarks = [marks1ststudent, marks2ndstudent, marks3rdstudent, marks4thstudent, 
marks5thstudent]
SortedMarks.sort() # to sort the list in a order.
print(SortedMarks)

#QUESTION 5
#a) 
#create a list of colors
color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(color)
# (a) Python program to print a specified list after removing 4th element.
color.pop(3) # 3 is index to 4th element of color list
 print("output of part a is:")
print(color)

#b) Source code:-
# (b) Remove ‘Black’ and ‘Pink’ from the list and replace them with ‘Purple’.
# Do that in one line code.
# index of black is 3 and index of pink is 4
print("output of part b is:") 
color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color[3:5]=["Purple"] #replace 3 to 4 items to "Purple"
print(color)
