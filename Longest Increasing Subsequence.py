def longest_increasing_subsequence(nums):
  n=len(nums)
  dp=[1]*n
  for i in range(1, n):
    for j in range(i):
      if nums[j] < nums[i]:
        dp[i]=max(dp[i],dp[j]+1)
  return max(dp)
nums=eval(input("Enter List:"))
length=longest_increasing_subsequence(nums)
print(length)
