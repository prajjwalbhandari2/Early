i = [1, 2,3, 4,5,6]
def func(num):
    return num ** 2
print(list(map(func,i)))
for x in i:
    print(x)
