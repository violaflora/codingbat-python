def double_char(str):
  newStr = ''
  for char in str:
    newStr += char + char
  return newStr

def count_hi(str):
  count = 0
  for i in range(len(str)-1):
    if str[i:i+2] == 'hi':
      count += 1
  return count

def cat_dog(str):
  catCount = 0
  dogCount = 0
  for i in range(len(str)):
    if str[i:i+3] == 'cat':
      catCount += 1
    if str[i:i+3] == 'dog':
      dogCount += 1
  return catCount == dogCount

def count_code(str):
  count = 0
  alts = codeAlts()
  for i in range(len(str)-3):
    if str[i:i+4] in alts:
      count += 1
  return count
  
def codeAlts():
  codeAlts = []
  az = 'abcdefghijklmnopqrstuvwxyz'
  for letter in az:
    codeAlts.append('co' + letter + 'e')
  return codeAlts

def end_other(a, b):
  a = a.lower()
  b = b.lower()
  return b == a[-len(b):] or a == b[-len(a):]

def xyz_there(str):
  xyzCount = 0
  for i in range(len(str)):
    if str[i:i+3] == 'xyz':
      xyzCount += 1
      if str[i-1] == '.':
        xyzCount -= 1
  if xyzCount > 0:
    return True
  return False