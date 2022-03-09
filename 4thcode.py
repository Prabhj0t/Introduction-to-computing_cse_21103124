# Ques 4
print("CODE OF 4th")
#function of partition..


def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# quick sort function..


def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


n = int(input("ENTER the no. of element you want list of..:\n"))
li = list(map(int, input(
    "Enter the integers with a blank spaces but without commas:\n").strip().split()))
quickSort(li, 0, n - 1)
print("Your Sorted array is: ", li)
