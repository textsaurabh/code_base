class Solution:
    # @return an integer
    def reverse(self, x):
        negative = False
        if x < 0 : 
            x *= -1
            negative = True
            
        rev_num = 0
        while(x > 0):
            rev_num = rev_num * 10 + x % 10
            x /= 10
            
        return rev_num * -1 if negative else rev_num

if __name__ == '__main__':
    Solution().reverse(-82314)
