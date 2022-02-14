    # QUESTION 1
a = str(input("Enter the String you want: "))
list = a.split()  # split string to elements in list
print(list)  # print list
dict = {}  # initialize an empty dictionary
if list.__len__() == 1:  # condition if string has one character only
    for i in list[0]:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    print(dict)
else:  # else statement for more than one word string
    for i in list:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    print(dict)

# QUESTION 2
while(True):  # using while loop to take correct value from user if wrong them may take again
    day = int(input("Enter the Day: "))
    if(1 <= day <= 31):
        break
    else:
        print("**Please Enter day from 1 to 31**")
while(True):
    month = int(input("Enter The Month of the year: "))
    if(1 <= month <= 12):
        break
    else:
        print("**Please Enter a valid month from 1 to 12**")
while(True):
    year = int(input("Enter the Year: "))
    if(1800 <= year <= 2025):
        break
    else:
        print("**Please Enter year from 1800 to 2025 only**")
if(month == 2):

    if(((year % 400 == 0) and (year % 100 == 0))  # condition for century years to be leap year
       or (year % 100 != 0) and (year % 4 == 0)):  # condition for non century years
        print("This is leap year")
        if(day == 29):  # last day of feb. month of leap year
            day = 1
            month = month+1
            print(day, "/", month, "/", year)
        elif(day < 29):
            day += 1
            print("NEXT DATE IS:", day, "/", month, "/", year)
       
    else:
        if(day == 29):
            print("Sorry this is not a leap year SO, max day in feb is 28,**please enter the othentic information**")
        elif(day == 28):  # last day of feb. month
            day = 1
            month += 1
            print("NEXT DATE IS:", day, "/", month, "/", year)
        elif(day < 28):
            day += 1
            print("NEXT DATE IS:", day, "/", month, "/", year)

elif(month % 2 != 0 and 1 <= month <= 12):  # condition only on the month having 31 days ODD months
    if(day == 31):  # last day of month
        day = 1
        month = month+1
        print("NEXT DATE IS:", day, "/", month, "/", year)
    elif(day < 31):
        day += 1
        print("NEXT DATE IS:", day, "/", month, "/", year)

elif(month % 2 == 0 and 1 <= month < 12):
    if(day == 30):
        day = 1
        month = month+1
        print("NEXT DATE IS:", day, "/", month, "/", year)
    elif(day < 30):
        day += 1
        print("NEXT DATE IS:", day, "/", month, "/", year)

elif(month == 12):
    if(day == 31):  # last day of year
        day = 1
        month = 1
        year += 1
        print("NEXT DATE IS:", day, "/", month, "/", year)
        print("WISHING YOU HAPPY NEW YEAR :)")
    elif(day < 31):
        day += 1
        print("NEXT DATE IS:", day, "/", month, "/", year)

else:
    print("**SOMETHING WENT WRONG**")


# QUESTION 3
my_list = []
# first specify the Size of List
Range = int(input("Enter the No. of elements you want list of :"))
for i in range(0, Range):  # entering the elements in list one by one by using for loop
    element = int(input("Enter the element in list :"))
    my_list.append(element)        # update list elements
    print(my_list)
print("Final list we have is:", my_list)
a = [(x, x**2) for x in (my_list)]  # intilize tuple as (x,x**2) power operator
print("The list of touples we have as output is :", a)


# QUESTION 4
grade_points = int(input("Enter Grade Points you earn between 4 to 10: "))
if(4 <= grade_points <= 10):
    if(grade_points == 10):
        grade = "A+"
        performance = "Outstanding"
    elif(grade_points == 9):
        grade = "A"
        performance = "Excellent"

    elif(grade_points == 8):
        grade = "B+"
        performance = "Very good"

    elif(grade_points == 7):
        grade = "B"
        performance = "Good"

    elif(grade_points == 6):
        grade = "C+"
        performance = "Average"

    elif(grade_points == 5):
        grade = "C"
        performance = "Below Average"

    elif(grade_points == 4):
        grade = "D"
        performance = "Poor"
    print("you Got", grade, "grade and", performance, "Performance")
else:
    print("***please Enter the correct othentic grade points***")  # error message


# QUESTION5
print("QUESTION 5")
x = 6
for i in range(x):
    for j in range(i):
        print(' ', end='')  # printing spaces
    for j in range(2*(x-i)-1):  # printing alphabet
        print(chr(65 + j), end='')  # Refers ASCII VALUE TABLE
    print()
print("\n")


# QUESTION6
print("QUESTION 6")
sid = int(input("Enter SID: "))
name = input("Enter Name: ")
students = {sid:name}

while True:
    option = input("Do you want to enter another student entry(Y or N):").upper()
    if option == 'Y':
        sid = int(input("Enter SID: "))
        name = input("Enter Name: ")
        students[sid] = name
    elif option == 'N':
        break
    else:
        print('Invalid input!')

#part a. print the dictionary
print("a:",students)

#part b. sort acc to the names
print("b:",{k:v for k,v in sorted(students.items(), key= lambda x:x[1])})

#part c. sort acc to the SIDs
print("c:",{k:v for k,v in sorted(students.items())})

#part d. search for a student by their SID
sid = int(input("Search Name with SID: "))
print("d:",students[sid])



# QUESTION 7
def fib(n):
    if (n <= 1):
        return n
    else:
        return(fib(n-1)+fib(n-2))


No_of_ternms = int(input("Enter the no. of terms you want series of:"))
Sum = 0
if (No_of_ternms <= 0):  # condition for filtring positive value only
    print("**please enter positive integer**")
else:
    print("The series is: ", end="")
    for i in range(No_of_ternms):
        print(fib(i), end=" ")
        Sum += fib(i)
average = float(Sum/No_of_ternms)
print("\naverage of final Fibonacci series is", average)


# Question 8
Set1 = {1, 2, 3, 4, 5}
Set2 = {2, 4, 6, 8}
Set3 = {1, 5, 9, 13, 17}
# part a
Set_Union = (Set1 | Set2)
Set_Intersection = (Set1 & Set2)
Set_A = Set_Union - Set_Intersection
print("part a:", Set_A)

# part b(Subtracting intersection of sets taken two at a time from the Union of all three sets)
Set_B = (Set1 | Set2 | Set3) - (Set1 & Set2) - (Set2 & Set3) - (Set3 & Set1)
print("part b:", Set_B)

# part c(Subtracting the intersection of all three sets from the Intersection of sets taken two at a time)
Set_C = (Set1 & Set2) | (Set1 & Set3) | (Set2 & Set3)-(Set1 & Set2 & Set3)
print("part c:", Set_C)
# part d(Excluding the numbers from 1 to 10 that are occuring in Set1)
Set_D = set()
for i in range(1, 11):
    if i not in Set1:
        Set_D.add(i)
print("part d:", Set_D)
# part e(Excluding the numbers from 1 to 10 that are occuring in Set1, Set2 and Set3)
Set_E = set()
for i in range(1, 11):
    if i not in (Set1 | Set2 | Set3):
        Set_E.add(i)
print("part e:", Set_E)
