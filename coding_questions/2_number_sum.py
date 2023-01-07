# Original brute force solution
# O(N^2)  Time
# O(N)    Space
# Given an array and a target sum, make a function that checks the array if there are 2 numbers that add
# up to the target sum. Return an array of both these numbers. if there are none return an empty array
def twoNumberSum(array, targetSum):
    for int in array:
        remain = targetSum - int
        if array.count(remain) and int != remain:
            return [int, remain]
    return []

arr = [1, 2, -3, 5, 6, 7]

print(twoNumberSum(arr, 4))      # Should return [-3, 7] because these 2 numbers add to 4