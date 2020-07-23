'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Your code here
    a_list = [] #create empty list
    for i in range(0,len(arr)): #go through list
        start = 1   # create a starting point for multiplication
        for n in arr:
            if n != arr[i]: #if the number being iterated through isn't itself
                start *= n  # multiply that number by everything in the list
        a_list.append(start) # append all the multiplications into the empty list
    return a_list
    

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
