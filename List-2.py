def count_evens(nums):
    evens = [num for num in nums if num % 2 == 0]
    return len(evens)

def big_diff(nums):
  return max(nums) - min(nums)

def centered_average(nums):
  nums.remove(min(nums))
  nums.remove(max(nums))
  return sum(nums) / len(nums)

def sum13(nums):
  for i in range(len(nums)-1):
    if nums[i] == 13:
      nums[i] = 0
      nums[i+1] = 0
  if len(nums) > 0 and nums[-1] == 13:
    nums[-1] = 0
  return sum(nums)

def sum67(nums):
  sum = 0
  zero = False
  for num in nums:
    if num == 6:
      zero = True
    if num == 7 and zero:
      zero = False
      continue
    if zero == False:
      sum += num
  return sum

def has22(nums):
  for i in range(len(nums)-1):
    if nums[i] == 2 and nums[i+1] == 2:
      return True
  return False