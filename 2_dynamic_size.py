# Dynamic size means our lists can grow and shrink by adding and removing items

bec_class = ['Dillon', 'Christy', 'Tony', 'Eric']
print(bec_class)


# ADDING TO LISTS

#--- list.append(item) : list method that adds an item to the END of the list

bec_class.append('Cole')
print(bec_class)

bec_class.append('Jason')
print(bec_class)

bec_class.append('Jesmarie')
print(bec_class)

another_list = [1,2,3,4]

bec_class.append(another_list)
print(bec_class)

# REMOVING FROM LISTS

#-- list.remove(item) : list method that allows us to remove an item by name

bec_class.remove(another_list)
print(bec_class)

bec_class.remove('Eric')
print(bec_class)

bec_class.remove('Jesmarie')
print(bec_class)