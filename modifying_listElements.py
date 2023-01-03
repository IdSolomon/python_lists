# To change a value in a list, I have to reassign the value using the specific index.

supermanGroceryList = ["eggs", "milk", "bread", "juice", "chicken", "beef", "ham", "cheese"]

supermanGroceryList[3] = "apples"
print(supermanGroceryList)

# OUTPUT: ['eggs', 'milk', 'bread', 'apples', 'chicken', 'beef', 'ham', 'cheese']
# The juice was replaced by apples unfortunately due to it having way too much sugar.

# Negative indices work as well --

supermanGroceryList[-1] = "cashew cheese"
print(supermanGroceryList)

# OUTPUT: ['eggs', 'milk', 'bread', 'apples', 'chicken', 'beef', 'ham', 'cashew cheese']