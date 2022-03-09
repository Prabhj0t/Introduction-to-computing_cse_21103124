# Ques 5
print("CODE of 5")
n = int(input("enter the number of integers to be entered:\n"))
li = list(map(int, input(
    "Enter the integers with space but without commas:\n").strip().split()))
# Part 1st
li.sort()
print("Sorted array is:", li)

# Part 2nd
flag = False
low = 0
high = n
count = 0
ind = -1
to_find = int(input(
    "Enter the integer from list whose index and times of occurances you want to find:\n"))
while(low < high):
    mid = low + (high - low) // 2
    if(int(li[mid]) == to_find):
        flag = True
        ind = mid
        print("Index of the value is:", mid)
        break
    elif li[mid] > to_find:
        high = mid - 1
    else:
        low = mid + 1
if flag == False:
    print("**Error**")

# Part 3rd
if(ind == -1):
    print("NO ELEMENT FOUND PLEASE CHECK\n")
else:
    i = mid
    j = mid
    count = 0
    for k in range(0, max(i, n - j)):
        if(i >= 0 and li[i] == to_find):
            count += 1
            i -= 1
        if(j < n and li[j] == to_find):
            count += 1
            j += 1
    print("Total times of occurances is:", count - 1)
