n = int(input())
nums = list(map(int, input().split()))

numSum = sum(nums)
nSum = n*(n+1)//2
print(nSum - numSum)