# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

def replaceElements(input):
    for i in range(len(input)-1):
        input[i] = (max(input[i+1:len(input)]))
    input[len(input)-1] = -1
    return input
print(replaceElements([17,18,5,4,6,1]))