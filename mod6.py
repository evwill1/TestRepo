# list

numbers = [1,2,3,4,5]
animals = ["dog", "cat", "horse", "fish", "gerbil"]
mixed = [1, "two", 3.0]
sublist = [[1,2,3],["one", "two", "three"],["I", "II", "III"]]
empty = []
 # print list
print(numbers)
print(sublist)
print(type(sublist))

print(len(numbers))
print(empty)
print(len(empty))
# indexing starts at 0
print(animals[4])
print(sublist[1][1])

#MODIFYING LIST

#adding elements
#appending (adds element to end of list)
my_list = [1,2,3]
print(my_list)
my_list.append(4)
print(my_list)

#insert (index and object)
my_list.insert(1,1.5)
print(my_list)

#removing elements (by object)
new_list = [1, 2, 3, 1, 2, 3]
print(new_list)
# new_list.remove(3)
print(new_list)

#Pop (removes an element by index(defaults to last index))
new_list.pop(5)
print(new_list)

#Del (removes an element at a specific index or a slice)
list = ["a", "b", "c", "d", "e", "f"]
print(list)
del list[0:6]
print(list)
# changing existing elements

#Re-assinging elements by index
ls = ["magic", "the", "gathering"]
print(ls)
ls[2] = "card game"
print(ls)

# Slicing & Looping through Lists

# Slicing

# Looping

# For ... in loop

# Using range() when you need indices

# Advanced List Operation

# .sort() - changes list in place

# .sorted() - 