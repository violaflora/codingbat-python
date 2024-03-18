def sleep_in(weekday, vacation):
  """
  #e.g. sleep_in(False, False)
  not weekday = True, vacation = False
  True or False → True
  """
  return not weekday or vacation

def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile or not a_smile and not b_smile:
    return True
  return False

def sum_double(a, b):
  if a == b:
    return ((a + b) * 2)
  return a + b

def diff21(n):
  absNDiff = abs(n-21)
  if n > 21:
    return absNDiff * 2
  return absNDiff

def parrot_trouble(talking, hour):
  return(talking and (hour < 7 or hour > 20))

def makes10(a, b):
  return(a == 10 or b == 10 or a + b == 10)

def near_hundred(n):
  return(n in range(90,111) or n in range(190,211))

def pos_neg(a, b, negative):
  if negative:
    return(a < 0 and b < 0)
  return(a * b < 0)

def not_string(str):
  if str.split()[0] == 'not':
    return str
  return('not ' + str)

def missing_char(str, n):
  return(str[:n] + str[n+1:])

def front_back(str):
  if len(str) < 2:
    return(str)
  return(str[-1] + str[1:-1] + str[0])

def front3(str):
  return(str[:3] * 3)