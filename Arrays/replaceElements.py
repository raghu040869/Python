# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

<<<<<<< HEAD
def replaceElements(input):
    for i in range(len(input)-1):
        input[i] = (max(input[i+1:len(input)]))
    input[len(input)-1] = -1
    return input
=======
def replaceElements(arr):
    for i in range(len(arr) - 1):
        arr[i] = (max(arr[i + 1:len(arr)]))
    arr[len(arr) - 1] = -1
    return arr
>>>>>>> 26554af (replaceelements)
print(replaceElements([17,18,5,4,6,1]))