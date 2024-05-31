# some cool things we can do with list methods

food = ['tacos', 'pizza', 'tiramisu']
print(food)

#-- list.append(item)

print("Adding ice cream")
food.append("ice cream")
print(food)

#-- list.insert(index, item) : allows us to add an item to a specific index
# adding to a list at an index that doesn't exist will simply put it at the end
print("Inserting a potato to our list of food")
food.insert(2, "potato")
print(food)

#-- list.remove(item)
print("Removing piza :(")
food.remove("pizza")
print(food)

#-- list.pop() : removes and returns the last item in the list
# just because it returns a value doesn't mean we have to collect the value in a variable
print("Putting ice cream in the freezer")
freezer = food.pop()
print("Freezer: ", freezer)
print(food)

#-- list.pop(index) : removes an item at a certain index
print("Popping our potato in the oven")
oven = food.pop(1)
print("Oven: ", oven)
print(food)

# Hit up the grocery store

food.append('burger')
food.append('bread')
food.append('cheese')
food.append('sushi')
food.append("key lime pie")
food.append('salad')

print('we went to the store')
print(food)

#-- list.index(item) : will return the index of a particular item
print('Finding the index of salad using .index()')
salad_idx = food.index('salad')
print('Salad position: ', salad_idx)

#-- Modify the values at a particular position/index. MUTABILITY list[index] = new_item
print("spicing up our salad.")
food[7] = 'caesar salad'
print(food)

food.append('burger')
print(food)

#-- list.count(item) : will count the occurances of an item in a list, return an int
print("counting burgers!...")
burger_count = food.count('burger')
print('Burger count: ', burger_count)

#-- list.reverse() : will reverse the order of your list
food.reverse()
print(food)

#-- list.sort() : will sort your list in ascending/alphabetical
# when sorting a list, all items must be of the same type 
print("sorting in alphabetical (abc) order")
food.sort()
print(food)

# Multiple data types do not work together when sorting
# test = [1, 'stringg', 3.14, food]
# test.sort()
# print(test)

#-- list.sort(reverse = True) : reverse sort, descending / zyx order
food.sort(reverse=True)
print(food)

#----------- List Functions

#-- len(item) : returns the length of the list aka how many items are in the list?
print("Length of our food list: ", len(food))


#-- sum(list) : give us the sum total of all numbers in a list
# list must be made entirely of ints or floats

nums = [1,2,3,4,5,6,4.4]
total = sum(nums)
print('Sum of nums in list: ', total)

mess = [False, True, False]
mess.sort()
print(mess)