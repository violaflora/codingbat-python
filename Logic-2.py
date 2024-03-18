def make_bricks(small, big, goal):
  if goal - (goal // 5 * 5) > small:
    return False
  if goal - 5 * big <= small:
    return True
  return False

def lone_sum(a, b, c):
  sum = 0
  if a != b and a != c:
    sum += a
  if b != a and b != c:
    sum += b
  if c != a and c != b:
    sum += c
  return sum

def lucky_sum(a, b, c):
  if a == 13:
    return 0
  if b == 13:
    return a
  if c == 13:
    return a + b
  return a + b + c

def no_teen_sum(a, b, c):
  return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):
  if n == 15 or n == 16:
    return n
  if n in range(13, 20):
    return 0
  return n

def round_sum(a, b, c):
  return round10(a) + round10(b) + round10(c)
  
def round10(num):
  return int(round(num, -1))

def close_far(a, b, c):
  #check for b close and c far
  if b in range(a-1, a+2) and (abs(c-a) >= 2 and abs(c-b) >= 2):
    return True
  # check for c close and b far
  if c in range(a-1, a+2) and (abs(b-a) >= 2 and abs(b-c) >= 2):
    return True
  return False

def make_chocolate(small, big, goal):
  if goal - (goal // 5 * 5) > small:
    return -1
  if goal - 5 * big <= small:
    if big * 5 <= goal:
      return goal - big * 5
    return goal - (goal // 5 * 5)
  return -1