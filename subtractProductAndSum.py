class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product=1
        sum=0
        while n!=0:
            last=n%10
            product*=last
            sum+=last
            n=n//10
        return product-sum
