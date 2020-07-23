'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # iterate through array and finds single int
    # return single int
    odd = arr[0]
    for i in range(1,len(arr)):
        odd ^=arr[i] # https://www.w3schools.com/python/python_operators.asp
                     # checks to see if each number matchs via a binary check
    return odd



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]
    print(f"The odd-number-out is {single_number(arr)}")
