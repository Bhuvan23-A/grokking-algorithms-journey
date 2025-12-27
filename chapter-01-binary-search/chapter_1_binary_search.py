def binary_search(list,item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high)// 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
    
my_lst = [1,3,5,7,9]
print (binary_search(my_lst, 3))
print (binary_search(my_lst, -1))

#EXERCISES
#1.1. log 128 to the base 2 -> 7 steps
#1.2. 8 steps


#1.3. O(n)
#1.4. O(n)
#1.5. O(n)
#1.6. 