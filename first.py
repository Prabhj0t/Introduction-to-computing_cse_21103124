# take input from student of his/her information name,course,SID,Gender,CGPA
# and make list of it as output

SID=int(input("Enter your StudentID:"))

Name=input("enter your Name:")

Gender=input("enter your Gender M/F/U:")

Course=input("enter your course you studing:")

CGPA=float(input("enter your CGPA:"))

Student =[SID,Name,Gender,Course,CGPA]

# now we printing the details

print("\n***STUDENT DETAIL***")

print(Student)
