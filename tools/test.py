# def climbStairs( n: int) -> int:
#     if n == 0:
#         return 0
#     dp = [0] * (n + 1)
#     dp[0] = 0
#     dp[1] = 1
#     for i in range(2, n + 1):
#         dp[i] = dp[i - 1] + dp[i - 2]
#     return dp[-1]
# a= climbStairs(2)
#
# print(a)
import sys,os
# os.removedirs('0507_mul/gray/1')
# print(sys.executable)
def A(b):
    b+=1
    return b
A(1)