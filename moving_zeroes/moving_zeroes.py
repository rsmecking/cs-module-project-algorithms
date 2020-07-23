'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    new = [] # list for numbers other than 0
    zeros = [] # list for 0's
    
    for i in range(len(arr)): # go through array
        if arr[i] == 0:       # if array contains 0
            if type(arr[i]) == int: # if the type is an int
                zeros.append(arr[i]) # if zeros append to zeros list
            else: new.append(arr[i]) # if anthing other than zero append to new list
        else:
            new.append(arr[i])
    return new + zeros # puts the two list together with zeros at end.
  
    


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")