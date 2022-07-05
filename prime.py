'''list = []
d = dict()
def number():
  num = int(input("Enter a number:"))
  while num < 2:
    num = int(input("Enter a number:"))
  return num
a = number()
def check(a):
    for n in range(2, a+1):
        for i in range(2,n):
            if (n % i) == 0:
                break
        else:
            list.append(n)
            d["List:"] = list
            d["Length:"] = len(list)
    return d
print(check(a))'''
