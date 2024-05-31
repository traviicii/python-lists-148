# Python Lists

# lists are a collection of items; mutable, ordered, and have dynamic sizing

#-- ordered : each item has a specific position, which allows us to know where each item is
#-- mutable : the ability to mutate lists; add, remove, manipulate data
#-- dynamic size : add and remove from lists allowing them to grow and shrink as we need

# Lists are created with [] square brackets, and each item inside of a list is separated by a ','

# empty list

empty_list = []

# populated list

person = 'Jill'

people = ['Bob', 'Barry', "Bernie", "Bill", person]

# Python lists can contain a variety of data types

stuff = [12, 'apple', False, 3.14, ['Dylan', 'Travis', ['tacos']]]

#---- List Indecies

# each item is marked by  specific index
# indices are in numeric order starting from 0, we can use indecies to access, modify, and remove items from our list

#indicies   0        1        2        3
alist = ['item1', 'item2', 'item3', 'item4']
print(alist)

# grab item 3 with index 2
print("Third item: ", alist[2])

# grab item 1 with index 0
print("Item 1, first item: ", alist[0])

# grab the last item using index 3
print("last item: ", alist[3])

# grab the last item using index -1
print("last item with index [-1]: ", alist[-1])

# potential pitfalls

# IndexError
#-- index out of range, trying to access an index that doesn't exist

# print(alist[4])