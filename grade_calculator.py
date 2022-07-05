name = input('Enter the name of student:')
roll = input('Enter roll number of student:')
phy = int(input("Enter marks obtained in Physics:"))
chem = int(input("Enter marks obtained in Chemistry:"))
maths = int(input("Enter marks obtained in Maths:"))
eng = int(input("Enter marks obtained in English:"))
nep = int(input("Enter marks obtained in Nepali:"))


total = (phy + chem + maths + eng + nep) 
per = total / 500 * 100
print('Student Details:')
print(f'{"Name:":10} {name}')
print(f'{"Roll no.:":10} {roll}')
print(f'{"Class:":10} XII \'S10\'')
print('\nAcademic Performance:')
print(f'\n{"Physics:":25} {phy}')
print(f'{"Chemistry:":25} {chem}')
print(f'{"Maths:":25} {maths}')
print(f'{"English:":25} {eng}')
print(f'{"Nepali:":25} {maths}')
print(f'\n{"Total Mark obtained:":25} {total}')
print(f'{"Percentage:":25} {int(per)} %')
if per > 90:
    print(f'\nThe grade obtained by {name} is A+.')
elif 80 < per <= 90:
    print(f'\nThe grade obtained by {name} is A.')
elif 70 < per <= 80:
    print(f'\nThe grade obtained by {name} is B+.')
elif 60 < per <= 70:
    print(f'\nThe grade obtained by {name} is B.')
elif 50 < per <= 60:
    print(f'\nThe grade obtained by {name} is C+.')
else:
    print(f'\n{name} failed.')


