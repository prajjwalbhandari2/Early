#radius = input("Enter the radius of circle:")
#Area = 3.142 * int(radius) ** 2
#print("The area of given circle is", Area)
#ninjas = ["Kapil", "Utsav", "Bikash"]
#for ninja in ninjas:
#  if ninja == "Kapil":
#       print(f'{ninja} - haat bhacheko')
#  elif ninja == "Utsav":
#     print(f'{ninja} - chabi birsine')
# else:
#     print(f'{ninja} - pagal')
#age = 20 
#num = 0
#while num < age:
#    if num % 2 == 0:
 #       print(num)
 #       if num >= 10:
 #           break
  #  num += 1
#fruits = ["apple", "banana", "guava"]
#print(fruits[0])
#x = "i"
#y = "am"
#z = "Prajjwal"
#print(x+y+z)
#def myfunc():
#    x = "Prajjwal"
    #print("I am", x)
#myfunc() 
#x = 5
#y = 7
#print(x, y)
'''def myfunc():
  global a
  a = {1,2,2,3,3,3}
  print(a)
myfunc()'''
'''num1 = 1
num2 = 2
print (" i want {}, {}". format(num1, num2))'''
"""from re import X

class
def _len_(self):
  return "I am Prajjwal"
  X = "Hello"
  print(X, )"""
"""a = input("Enter Your Age:")
a = int(a)
if a <= 12:
  print("You're a child.")
elif a <= 20:
  print("You're a teenager")
else:
  print("You're a adult")"""
'''a = ["Prajjwal", "apple", "banana"]
a[1]= "guava"
print(a)'''

"""x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
def myfunc():
  a = float(x)

#convert from float to int:
  b = int(y)

#convert from int to complex:
  c = complex(x)

  print(a)
  print(b)
  print(c)
myfunc()

print(x)
print(y)
print(z)"""
'''a = input("Enter the Day:")
if a == "sunday" or "sun" or "Sunday" or "Sun":
  print("Apple day")
else:
  print("Banana day")'''
'''def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]

thislist.sort(key = myfunc)

print(thislist)'''
"""listA = ["Apple", "facebook", "banana", "football"]
listB = tuple(listA)
print(listB)"""
'''thisset = {"apple", "banana", "cherry"}

thisset.remove(thisset[1])

print(thisset)'''
'''thisdict = {
  "name" : "Prajjwal",
  "year" : 2021,
  "age" : 19
}
print(thisdict.fromkeys(thisdict))'''

'''i = 0
while i < 6:
  i += 1
  print(i)
else:
  print("i is no longer less than 6")'''
'''i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)'''
'''i = 0
while i<10:
  i += 1
  if i == 5:
    continue
  print(i)
else:
  print("Finally finished!!")'''
'''def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)'''
'''import sys
print(sys.getrecursionlimit())'''
'''age = 15
num = 0
while num < age:
    if num == 5:
      num += 1
      continue
    print(num)'''
'''burgers = ['chicken', 'veg','mushroom', 'ham', 'mixed']
for x in range(len(burgers) -1, -1, -1):
  print(x, burgers[x])
def myfunc():
  burgers.sort(reverse=True)
  print(burgers)
myfunc()'''
'''mistake'''
'''def myfunc(area):
  r = input(int("Enter the radius of desired circle:"))
  A = 3.14 * r**2
  print(f'The Area of circle is {a}')
myfunc()'''
'''def area():
  radius = int(input("Enter the radius:"))
  print(3.14 * radius ** 2)
  def vol():
    length = int(input("Enter the length"))
    print(area * length)
  vol()
area()'''



'''class Planet:

  def __init__(self):
    n = input("Enter the name of Planet:")
    r = int(input("Enter the radius:"))
    g = float(input("Enter the gravity:"))
    ga = input("Enter the galaxy:")
    self.name = n
    self.radius = r
    self.gravity = g
    self.galaxy = ga

  def orbit(self):
    return (f"The planet {self.name} is orbiting in {self.galaxy}.")

Earth = Planet()
print(f"Details of Planet: \n{Earth.name} \n{Earth.radius} cm\n{Earth.gravity} m\s\u00b2")

print(Earth.orbit())'''

'''class Class:
suppose shape = "round" bhanera def ko bahira banaiyo
teslai access garna tala Class.shape use garey pani huncha ya student.shape lekhda pani huncha
  def __init__(self):
      n = input("Enter the name of student:")
      c = input("Enter their class:")
      r = input("Enter their roll number")
      d = input("Enter their illness:")
      self.name = n
      self.clasS = c
      self.roll_no = r
      self.illness = d

      @classmethod
      def commom(cls):
        print("...{cls.shape}...")
        yeslai access garna chai tala Class.common() ra student.common() dubai use garna milcha
      @staticmethod
      def spin (speed= "......")
      return ................{speed}
      Class.spin() or student.spin() parenthesis ma arko value rakhera teslai overwrite garna pani milcha
     
      
  def details(self):
      return f'{self.name} of class {self.clasS} having roll number {self.roll_number} is suffering from {self.illness}'
student = Class()
print("Details of Student:")
print(f"Name: {student.name}")
print(f'Class: {student.clasS}')
print(f'Roll No.: {student.roll_no}')
print(f'Illness: {student.illness}')
# details lai access garna tala student.details lekhnu parcha
print(student.details())'''
'''while True:
  n = input("Enter the name of student:")
  c = input("Enter their class:")
  r = input("Enter their roll number;")
  d = input("Enter their illness:")

  def printed():
    print("Details of Student:")
    print(f"Name: {n}")
    print(f'Class: {c}')
    print(f'Roll No.: {r}')
    print(f'Illness: {d}')
    print(f'{n} of class {c} having roll number {r} is suffering from {d}')
  printed()
  add = input("Do you another student?")
  if add in {"yes", "Yes", "y", "Y"}:
    continue
  if add in {"No", "no", "n", "N"}:
    break'''

'''student = {
  '1':{
    "name" : "Prajjwal",
    "class" : 12
  },
  "2":{
    'name': "abc",
    "class" : 12,

  }

}
for i in student:
  print (student[i])'''
'''student = {

} 
n = input("Enter the name of student:")
c = input("Enter their class:")
r = input("Enter their roll number;")
d = input("Enter their illness:")'''

'''class bill:

  menu = {
    'momo': 100,
    'pizza' : 500,
    'cold_drinks' : 50,
    'burger' : 100,
    'sizzler' : 300
  }
  def __init__(self):
    self.total = 0
    self.ordered_items = []

  def join(self, item):
    self.ordered_items.append(item)
    self.total += self.menu[item]
  
  def print_bill(self):
    tax = int(input('Enter the tax percentile:'))
    tax_amt = (tax/100) * 100
    service = int(input('Enter the tax percentile:'))
    service_amt = (service/100) * 100
    total = self.total + tax_amt + service_amt

    
    print("Total Bills:")
    for item in self.ordered_items:
      print(f'{item:20} ${self.menu[item]:.2f}')
    print(f'{"Tax":20} ${tax_amt:.2f}')
    print(f'{"Service Charge":20} ${service_amt:.2f}')
    print(f'{"Total" :20} ${total:.2f}')'''

'''from random import shuffle
def jumble(word):
  anagram = list(word)
  shuffle(anagram)
  return "-".join(anagram)

def single_words(alphabet):
  anagram = list(alphabet)
  shuffle(anagram)
  return anagram

  
words = ['facebook', 'twitter', 'instagram']
anagrams = []
for word in words:
  anagrams.append(jumble(word))
  print(anagrams)
print([jumble(word) for word in words])
print(list(map(jumble,words)))
map(function,iterable)
function chai jun function pass garnu parne tyo
iterable chai jun list tuple or anything which is to be mapped
print(list(map(single_words,words)))'''
'''Decorator 
nam = input("Enter Your Name:")
def conversation(func):

  def decorate():
    print("Can I know your name?")
    func()
    print(f'Nice to meet you, {nam}')
  decorate() [ decorate() bhanera close garey pani huncha nagarey pani huncha]

  return decorate()

@conversation
def name():
  print(f'My name is {nam}')
'''
'''with open('write.txt', 'w') as file:
  file.write("Jay Nepal!!!")
'''
'''from random import randint
x = randint(0,6)
print(x)'''
'''a = "Prajjwal"
print(*a[::-1])
for x in range((len(a)) -1, -1, -1):
  print(a[x], sep=" " , end= ' ', flush=True)'''
'''a = "Prajjwal Bhandari"
for x in range(len(a)):
  print(a[x], end=" ", sep= ' ') 
print(a[0:-1])'''
'''a = [1,2,3,4,5,6,7,8,9,11,15,20,36]
for n in a:
  if n % 2 == 0:
    print(n , sep=" ", end= ",")'''
'''a = "Prajjwal Bhandari"
for letter in a:
  if letter == "a":
    continue
  print(letter)
b = a[:2] + a[3:]
print(b)'''
'''joins A and B in a tuple
A = [1,2,3]
B = ["x", "y" , "z"]
for x in zip(A,B):
  print(x)'''
'''from re import A

def area(radius):
  A = 3.14 * radius ** 2
  print("The area is", A, "cm\u00b2" + ".")
  return A

def vol(area, length):
  V = area * length
  print("The volume is", V, "cm\u00b3" + ".")

radius  = int(input("Enter the radius in cm:"))
length = int(input("Enter the length in cm:"))

area_calc = area(radius)
vol(area_calc, length)'''



'''fruits = {}
while True:
    type = input("Enter the type:")
    name = input("Enter the name of fruit:")
    fruits[type] = name

    add = input("add another?")
    yes = {"y", "Yes", "yes", "Y"}
    no = {"n", "no", "No", "N"}
    if add in yes :
        continue
    elif add in no:
        print(fruits)
    break'''
'''burgers = ['chicken', 'veg','mushroom', 'ham', 'mixed']
def myfunc():
  y = sorted(burgers, reverse=True)
  print(y)
myfunc()
for x in range(len(burgers) -1, -1, -1):
    print(x, burgers[x])'''



'''class Test:
    def __init__(self):
        self.name = " Prajjwal"
        self.full_name = 'name, {}'.format(self.name)

    def print_name(self):
        print(self.full_name)

my_object = Test()
my_object.name = 'my_object'

my_object.print_name()'''

'''grades = [ "A+", "A", "B+", "B", 'C+', 'C']
def failing_grade(grade):
  return grade != "B"
print(list(filter(failing_grade, grades)))'''
'''a = []
for x in range(1,51):
  if x%3 == 0:
    a.append(x)
print(a)    '''

'''for i in range(1,6):
  print('*' * i)'''





'''a =[" ", " ", " ", " ", " "," "]
for i in range(5,-1,-1):
  for x in range(5,i,-1):
    a[x] = '*'
  b = ' '.join(a)
  if b == "           ":
    pass
  else:
    print(b)


height = 5
for row in range(1, height+ 1):
    print(" " * (height - row) +"*" * row)'''


'''from cmath import pi


class Circle():
  #class object attribute
  pi = 3.14

  def __init__(self):
    radius = int(input("Enter the redius of the circle:"))
    self.radius = radius

  def circumference(self):
    cir = 2 * self.pi * self.radius      #self.pi ko sattaa Circle.pi lekhna pani paiyo 
    return f'The circrumference of circle is {cir}'
a = Circle()
print(a.circumference())'''

from unicodedata import name


class Animal():
  def __init__(self,name):
    self.name = name
  
  def speak(self):
    raise NotImplementedError('Subclass must be implemented!')

class dog(Animal):
  def speak(self):
    return f'{self.name} says woof!'
fido = dog('Fido')
print(fido.speak())

class cat(Animal):

  def speak(self):
    return f'{self.name} says meow!'
isis = cat('Isis')
print(isis.speak())
    