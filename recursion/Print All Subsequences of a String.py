# What is a Subsequence?
# A subsequence is a sequence derived from a string where you can delete 0 or more characters without changing the order.
# Example:
# For "abc", the subsequences are:
# "", "a", "b", "c", "ab", "ac", "bc", "abc"
# For a string of length n, there are 2^n subsequences
def subsequences(arr, index, current):
    #base case
    if index == len(arr):
        print(current)
        return
    #recursive case
    
    #include
    subsequences(arr, index + 1, current + [arr[index]])
    
    #exclude
    subsequences(arr, index + 1, current)
    
subsequences([1, 2, 3], 0, []) 
    