# Original brute force solution
def twoNumberSum(array, targetSum):
    for int in array:
        remain = targetSum - int
        if array.count(remain) and int != remain:
            return [int, remain]
    return []
