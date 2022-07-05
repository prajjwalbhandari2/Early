''''
First qn
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
def num(a,b):
  if a% 2 ==0 and b % 2 == 0:
    return f'The lesser number is {min(a,b)}'
  else:
    return f'The greater number is {max(a,b)}'
a = num(a,b)
print(a)'''
'''
Second project

a = input("Enter the two-word string:")
def check_word(a):
  x = a.split()
  if x[0][0].lower() == x[1][0] or x[0][0] == x[1][0].lower() or x[0][0] == x[1][0]:
    return True
  else:
    return False
   

b = check_word(a)
print(b)'''
''' 
third project
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
def check(a,b):
  arko tarika: return sum((a,b)) == 20 or 20 in (a,b) eti garey pugyo
  if sum((a,b)) == 20 or 20 in (a,b):
    return True
  else:
    return False


print(check(a,b))'''

''' 4th project


import re


a = input("Enter name: ")
def capital(a):
  b = a[0]
  c = a[1:3]
  d = a[3]
  e = a[4:]
  return b.upper() + c + d.upper() + e

print(capital(a))'''

''' 4th projrct
a = input("Enter the sentence:")
def check(a):
  x = a.split()
  y = x[::-1]
  return " ".join(y)
print(check(a))'''



'''modified program:::: this does not input number above 210
def check():
  num = int(input("Enter a number:"))
  while num not in range(211):
    num = int(input("Enter a number:"))
  return num
a = check()
def final(a):
    return (90 <= a <= 110) or (190 <= a <= 210)
print(final(a))

My ans to this qn::::
num = int(input("Enter a number:"))
def check(num):
  return (90 <= num <= 110) or (190 <= num<= 210)
print(check(num))

original ans:::
n = int(input("Enter the number:"))
def myfunc(n):
  return (abs(100-n) <= 10) or (abs(200-n) <= 10)
print(myfunc(n))'''


'''Level 2 2nd func matra ho ans 1st func chai input ko lagi:
list = input('Enter a list of number separated by space')

def lis(list):
  new_list = list.split()
  for i in range(len(new_list)):
    new_list[i] = int(new_list[i])
  return new_list
update = lis(list)

def check(update):
  for i in range(0,len(update)-1):
    if update[i] == 3 and update[i+1] == 3:  if update[i:i+2] == [3,3] pani garna milyo
      return True
  return False
print(check(update))'''

''' tripling each letter in a string

name = input("Enter Your Name:")
def tripling(name):
  result = ''
  for i in name:
    result += i * 3
  return result
print(tripling(name)) '''




''' my ans:

list = input('Enter a list of three integers between 1 and 11 separated by space:')

def lis(list):
  new_list = list.split()
  for i in range(len(new_list)):
    new_list[i] = int(new_list[i])
  return new_list
update = lis(list)

def check(update):
  for i in range(len(update)):
    if update[i] == 11:
      if sum((update)) - 10 >= 21:
        return "Bust"
      else:
        return sum(update) - 10
    elif sum((update)) >= 21:
      return "Bust"
    elif sum((update)) <= 21:
      return sum((update))
 
print(check(update))'''

'''
Actual ans


list = input('Enter a list of three integers between 1 and 11 separated by space:')

def lis(list):
  new_list = list.split()
  for i in range(len(new_list)):
    new_list[i] = int(new_list[i])
  return new_list
update = lis(list)

def check(update):
  if sum((update)) <= 21:
    return sum((update))
  elif 11 in update and sum((update)) <= 31:
    return sum((update)) - 10
  else:
    return "Bust"

print(check(update))'''



'''very hard ans
list = input('Enter a list of numbers seperated by space:')

def lis(list):
  new_list = list.split()
  for i in range(len(new_list)):
    new_list[i] = int(new_list[i])
  return new_list
arr = lis(list)

def summer_69(arr):
  total = 0 
  add = True

  for num in arr:
    while add:
      if num!= 6:
        total+=num
        break
      else:
        add = False
    while not add:
        if num!=9:
          break
        else:
          add = True
          break
  return F'The total is {total}'
print(summer_69(arr))'''


'''aayush  dai le sikaunu bhako process 1
list = input('Enter a list of numbers seperated by space:')

def lis(list):
  new_list = list.split()
  for i in range(len(new_list)):
    new_list[i] = int(new_list[i])
  return new_list
arr = lis(list)

def summer_69(arr):
  total = 0 
  add = True
#[1 2 3 4 6 7 8 9 6]
  for num in arr:
    while add:
      if num== 6:
        total+=num
        break
      else:
        add = False
    while not add:
      if num==9:
        add=True
        break
      else:
        break
  return F'The total is  {total}'
print(summer_69(arr))'''


''' aayush dai le sikaunu bhako process 2 

list = input('Enter a list of numbers seperated by space:')
def lis(list):
  new_list = list.split()
  for i in range(len(new_list)):
    new_list[i] = int(new_list[i])
  return new_list
arr = lis(list)

def summer_69(arr):
  total = 0 
  add = True
#[1 2 3 4 6 7 8 9 6]
  for num in arr:
    while add:
      if num== 6:
        add = False
      else:
        total+=num
        break

    while not add:
      if num==9:
        add=True
        break
      else:
        break
  return F'The total is  {total}'
print(summer_69(arr))'''


'''from cmath import inf
import math

inf = float(inf)
ran = range(0,inf)

for i in ran:
  total = [2 * (2 ** 0.5) * math.factorial(4*ran) * {1103 + (26390 * ran)} ] / [9801 * {(math.factorial(ran)) ** 4} * {(396)**(4*ran)}]
print(total)'''



