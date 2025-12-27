#4.1 
def sum_using_d_n_c(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    sum = arr[0] + sum_using_d_n_c(arr[1:])
    return sum 

print(sum_using_d_n_c([-1,2,3, 5,9]))


#4.2
def count_using_d_n_c(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return 1
    
    count = 1 + count_using_d_n_c(arr[1:])
    return count

print(count_using_d_n_c([-1,2, 5,9]))

#4.3
def max_using_d_n_c(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max

print(max_using_d_n_c([-1,2, 5,0]))

#4.4

''' Binary Search is also a divide and conquer algorithm.
The base case for Binary Search is when you try to match the item we are looking for with 
middle element. If it matches then we found it or else we do not have that element in the array

The recursive case for Binary search is when we divide the array into two halves and 
run the binary search on the array where there is a chance that the element we need would be present. 
'''

#QUICK SORT
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        lesser = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i >= pivot]

        return quick_sort(lesser) + [pivot] + quick_sort(greater)
    
print(quick_sort([9,1,8,5]))

#4.5
# for printing each element in the array n*O(1) = O(n)

#4.6
# Doubling each value also takes O(n) [O(n)*(O(1))]

#4.7
# For doubling only first element it will take O(1)[O(1)+ O(1) = O(1) for accessing 1st element and doubling constant time]

#4.8
# It will take O(n^2), O(n) for multiplying with 2 and so on for n elements we multiply ==> O(n)* O(n) = O(n^2)

