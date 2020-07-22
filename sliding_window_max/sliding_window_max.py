'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    ans = []
    queue = []
    for i, v in enumerate(nums):
        if queue and queue[0] <= i - k:
            queue = queue[1:]
        while queue and nums[queue[-1]] < v:
            queue.pop()
        queue.append(i)
        if i + 1 >= k:
            ans.append(nums[queue[0]])
    return ans

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
