def find_minimum(arr):

    min_number = arr[0] #assigns the first element as the lowest
    for num in arr: #checks through each number in the array until it knows its the lowest
        if num < min_number: #if the new number is lower than the previous assigned number
            min_number = num #the new number is the lowest
    return f"Minimum: {min_number}"
    
list1 = [5, 4, 9, 1, 3]  #output should be 1

print (find_minimum (list1)) 
