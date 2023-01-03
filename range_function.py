# range() is a built-in function I can use to easily create 
# a list containing the numbers 0 through 13 for example.

numberList = range(13)
print(list(numberList))

# OUTPUT: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# list() is another built-in function that takes in a single input 
# for the object you want to convert.

rangeList = range(13)
print(rangeList)

# OUTPUT: range(0, 13)
# This is something different - The range() function is unique in that it creates 
# a range object. It is not a typical list like the ones I have been working with.