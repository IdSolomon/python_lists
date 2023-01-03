# Slicing syntax in Python is very flexible.
# This means I'm taking the same syntax and tweaking it.

favoriteFruits = ["strawberry", "banana", "mango", "blueberry", "raspberry", "peach"]
print(favoriteFruits[:3])

# OUTPUT: ['strawberry', 'banana', 'mango']
# This new, tweaked syntax, favoriteFruits[:3], starts slicing from index 0 up to index 3.

print(favoriteFruits[3:])

# OUTPUT: ['blueberry', 'raspberry', 'peach']
# Slicing from index 3 up to the last index.

print(favoriteFruits[:-2])

# OUTPUT: ['strawberry', 'banana', 'mango', 'blueberry']
# Negative indices can also accomplish taking all but the last two elements of a list.

print(favoriteFruits[-2:])

# OUTPUT: ['raspberry', 'peach']
# This slices from the element at index -2 up through the last index.