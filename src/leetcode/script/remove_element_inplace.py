#! /usr/local/bin/python -u

# Given an array and a value, remove all instances of that value in place and return the new length.
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        if not A:
            return len(A)
            
        curr_idx = 0
        total_array_len = len(A)
        while (curr_idx <= total_array_len - 1):
            if A[curr_idx] == elem:
                del A[curr_idx]
                total_array_len -= 1
            else:
                curr_idx += 1
                
        return total_array_len

if __name__ == '__main__':
    main([1], 1)
