class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        quotient = 0
        negative = False
        if dividend < 0:
            dividend *= -1
            negative = True
            
        if divisor < 0:
            divisor *= -1
            negative = False if negative else True
            
        while (divisor < dividend):
            quotient += 1
            dividend -= divisor
            
        return quotient * -1 if negative else quotient

if __name__ == '__main__':
    print Solution().divide(42, 5) 
