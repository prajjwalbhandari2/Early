#TAKING A LIST AS INPUT FROM USER  

input_string = input('Enter elements of a list separated by space ')
print("\n")
user_list = input_string.split()
# print list
print('list: ', user_list)

# convert each item to int type
for i in range(len(user_list)):
    # convert each item to int type
    user_list[i] = int(user_list[i])

# Calculating the sum of list elements
print("Sum = ", sum(user_list))



#new program testing the class of object inside a list:
list = input("Enter a list of number separated by space")
new_list = list.split()
for i in range(len(new_list)):
    new_list[i] = int(new_list[i])
print(new_list)
x = type(new_list[0])
print(x)