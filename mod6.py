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
list = ["potatoes", "grapes", "milk", "eggs", "bread", "oranges"]
print(list[1:3])
print(list[:3])
print(list[1:])
print(list[1:6:2])


# Looping

# For ... in loop
for element in list:
    print(element) #print 1 element per line

# Using range() when you need indices
for i in range(len(list)):
    print(i, list[i])

names = ["Alice", "Bob", "Jane"]

for name in names:
    print("Hello, " , name, sep="")
# Advanced List Operation
numbers = [5, 2, 9, 1, 8, 4, 3, 2, 7, 3]
food = ["broccoli", "apple", "lettuce", "cucumber", "tomato", "raspberry", "onion", "dill", "basil"]

# .sort() - changes list in place
numbers.sort()
print(numbers)
food.sort()
print(food)
numbers.sort(reverse=True)
print(numbers)

# .sorted() - 
sorted_numbers = sorted(numbers)
print(numbers)
print(sorted_numbers)

# .reverse()
numbers.reverse()
print(numbers)
food.reverse()
print(food)

# min(), max(), sum()
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# .index()
onion = food.index("onion")
print(onion) #reverse and then count 0, 1, 2 onion = index 2
three_index = numbers.index(3)
print(three_index) #sorted and then count to first 3. 0, 1, 2, 3