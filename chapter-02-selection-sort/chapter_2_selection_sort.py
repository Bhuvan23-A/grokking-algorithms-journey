#2.1. Linked Lists bcoz it takes constant time for insertion

#2.2. Linked Lists are better for this bcoz u do sequential access

#2.3. Arrays are better for tasks like random accessing

#2.4. There might not be enough contiguous space to insert all the new users

#2.5. Searching would be slower than array but faster than LL but inserting would be faster than array but slower than LL


## SELECTION SORT
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(0, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print (selectionSort([5, 3, 6, 2, 10]))
