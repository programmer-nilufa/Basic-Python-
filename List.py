numbers = [1,2,5,7,3,9]
negetive_numbers = [-5,-9,-1]
    #The append() method adds an item to the end of the list
"""
 numbers.append(4)
 """
    #The index() method returns the index of the specified element in the list
"""
numbers = numbers.index(5)
"""
    #The list pop() method removes the item at the specified index
"""
item = numbers.pop(2)
print(item)
print(numbers)
"""
    #The remove() method removes the first matching element
"""
numbers.remove(5)
print(numbers)
"""
    #The extend() method adds all the items of the specified iterable, such as list, tuple, dictionary, or string , to the end of a list.
"""
numbers.extend(negetive_numbers)
print(numbers)
"""