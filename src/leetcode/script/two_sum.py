class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        # First lets enumerate the input array
        num_dict = dict(enumerate(num))

        # Create an array from value to indices
        rev_num_dict = {}
        for idx, val in num_dict.iteritems():
            if val not in rev_num_dict:
                rev_num_dict[val] = [idx]
            else:
                rev_num_dict[val].append(idx)
        
        # Now next step is just to find the values
        # which sums up to target
        for val, idx_arr in rev_num_dict.iteritems():

            # First case is when val is same as target-val
            # or target = 2 * val. In such a case, the
            # val should be present equal to or more than 
            # twice in the input array. We need to return
            # the first two occurrences
            if target-val == val:
                ret_val = [idx_arr[0]+1, idx_arr[1]+1]
                break

            # If target-val is different from val, just
            # return the first two occurences
            if target-val in rev_num_dict:
                ret_val = sorted([idx_arr[0]+1, rev_num_dict[target-val][0]+1])
                break
                
        return tuple(ret_val)

if __name__ == '__main__':
    Solution().twoSum([0, 4, 3, 0], 0) 
