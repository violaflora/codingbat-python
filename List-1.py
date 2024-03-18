def first_last6(nums):
  return(nums[0] == 6 or nums[-1] == 6)

def same_first_last(nums):
  return(len(nums) >= 1 and nums[0] == nums[-1])

def make_pi():
  return[3,1,4]

def common_end(a, b):
  return(a[0] == b[0] or a[-1] == b[-1])

def sum3(nums):
  return sum(nums)

def rotate_left3(nums):
  return[nums[1], nums[2], nums[0]]

def reverse3(nums):
  return nums[::-1]

def max_end3(nums):
  maxEnd = max(nums[0], nums[2])
  return[maxEnd, maxEnd, maxEnd]

def sum2(nums):
  if len(nums) < 2:
    return sum(nums)
  return nums[0] + nums[1]

def middle_way(a, b):
  return[a[1], b[1]]

def make_ends(nums):
  return[nums[0], nums[-1]]

def has23(nums):
  return 2 in nums or 3 in nums