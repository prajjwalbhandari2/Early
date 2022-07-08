lis = input('Enter the numbers separated by space:')
listA = lis.split()
for i in range(len(listA)):
    listA[i] = int(listA[i])
print('Sum =', sum(listA))