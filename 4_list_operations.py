# other cool thigns we can do with lists

# Mebership checks with 'in' to check if an item is in a list, return a boolean value

guest_list = ['Adam', 'Bob', 'Charlie', 'Dylan', 'Ethan']

print("Albert" in guest_list)
print('Dylan' in guest_list)

# name = input('What is your name? ')

guest_list.append('Travis')

# using if statements for membership check
# if name in guest_list:
#     print("Welcome to the party: ", name)
# else:
#     print("Sraamammm punk!!")

# Merging two lists with '+'

list1 = [1,2,3,4]
list2 = [5,6,7,8]
list3 = list1 + list2
print(list3)

# Copying a list with the .copy() method
# changes we make to a true copy do not affect the original list
fruit = ['apple', 'banana', 'orange']
copy_fruit = fruit.copy()
print(copy_fruit)
copy_fruit.pop()
print("copy_fruit: ", copy_fruit)
print("fruit: ", fruit)

# Copying a list with a full slice list[:]
fruit = ['apple', 'banana', 'orange']
copy_fruit = fruit[:]
print(copy_fruit)
copy_fruit.pop()
print("copy_fruit: ", copy_fruit)
print("fruit: ", fruit)

# common mistakes when copying a list, setting one list equal to another

nums = [1,2,3,4]
dums = nums
dums.pop()
print("dums: ", dums)
print("nums: ", nums)

# all this does is point to the same place in memory
# 1 piece of data with 2 names

#----------------------#

# Identity operators 'is' and 'is not', return a boolean value
# checking to see if two variables occupy the same location in memory

fruit = ['apple', 'banana', 'orange']
copy_fruit = fruit[:]

print(fruit is copy_fruit)
print(fruit == copy_fruit)

nums = [1,2,3,4]
dums = nums

print(dums is nums)

# List slicing list[start:stop] : return a sublist from the start index to the stop index
# default for start and stop are the beginning and the end of the list
# the stop index is non-inclusive, meaning the item at the stop index will not be included in the slice
# indecies         0          1         2         3
key_lime_pie = ['slice1', 'slice2', 'slice3', 'slice4']
# neg indecies     -4        -3        -2        -1
my_slice = key_lime_pie[0:1]
print(my_slice)

big_slice = key_lime_pie[1:3]
print(big_slice)

last_slice = key_lime_pie[3:]
print(last_slice)

last_slice2 = key_lime_pie[2:-1]
print(last_slice2)

last_slice3 = key_lime_pie[-1:]
print(last_slice3)

last_slice4 = key_lime_pie[-2:]
print(last_slice4)

# By indicating our start value at a negative index [-2] and not specifying an end value [-2:] we end up including everything from the [-2] index (also index [2])all the way to the end of our list, including the last value.

# Joining a list of strings together using ' '.join(list)

words = ['Hello', "I'm", "getting", "joined!"]

sentence = ' '.join(words)
print(sentence)

new_sentence = '!!!!!!'.join(words)
print(new_sentence)




#------ TESTING 123 ------#
list1 = [1,2,3,4,5]
list2 = [4567,3,5,7,8]
list3 = list1 + list2
result = ' '.join(str(list3))
print(result)
print("data type: ", type(result))

empty = []

for item in list3:
    empty.append(str(item))

ans = ''.join(empty)
print(ans, type(ans))

# some change here