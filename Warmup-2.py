def string_times(str, n):
  return str * n

def front_times(str, n):
  return str[:3] * n

def string_bits(str):
  result = ''
  for i in range(len(str)):
    if i % 2 == 0:
      result += str[i]
  return(result)

def string_splosion(str):
  result = ''
  for i in range(len(str)+1):
    result += str[:i]
  return(result)

def last2(str):
  if len(str) <= 3:
    return 0
  count = 0
  for i in range(len(str)-2):
    if str[i:i+2] == str[-2:]:
      count += 1
  return count

def array_count9(nums):
  count = 0
  for num in nums:
    if num == 9:
      count += 1
  return count

def array_front9(nums):
  return 9 in nums[:4]

def array123(nums):
  for i in range(len(nums)-2):
    if nums[i:i+3] == [1,2,3]:
      return True
  return False

def string_match(a, b):
  count = 0
  for i in range(len(a)-1):
    if a[i:i+2] in b[i:i+2]:
      count += 1
  return count