'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    new = []
    zeros = []
    
    for i in range(len(arr)):
        if arr[i] == 0:
            if type(arr[i]) == int:
                zeros.append(arr[i])
            else: new.append(arr[i])
        else:
            new.append(arr[i])
    return new + zeros
  
    


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")