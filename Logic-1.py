def cigar_party(cigars, is_weekend):
  if is_weekend:
    return cigars >= 40
  return cigars in range(40, 61)

def date_fashion(you, date):
  if you <= 2 or date <= 2:
    return 0
  elif you >= 8 or date >= 8:
    return 2
  return 1

def squirrel_play(temp, is_summer):
  if is_summer:
    return temp in range(60, 101)
  return temp in range (60, 91)

def caught_speeding(speed, is_birthday):
  if is_birthday:
    speed -= 5
  if speed in range(61, 81):
    return 1
  if speed >= 81:
    return 2
  return 0

def sorta_sum(a, b):
  sum = a + b
  if sum in range(10, 20):
    return 20
  return sum

def alarm_clock(day, vacation):
  if vacation:
    if day == 6 or day == 0:
      return "off"
    return "10:00"
  if day == 6 or day == 0:
    return "10:00"
  return "7:00"

def love6(a, b):
  return(a == 6 or b == 6 or a+b == 6 or a-b == 6 or b-a == 6)

def in1to10(n, outside_mode):
  if outside_mode:
    return(n <= 1 or n >= 10)
  return n in range(1, 11)

def near_ten(num):
  mod10 = num % 10
  return(mod10 in range(0, 3) or mod10 in range(8, 11))