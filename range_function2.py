# By default, range() creates a list starting at 0. 
# However, if we call range() with two inputs, we can create a list that starts at a different number.
# Here I have range(2, 20), which would generate numbers starting at 2 and end at 19 --
# just before 20.

myList = range(2, 20)
print(list(myList))

# OUTPUT: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# Now, if I use a third input, I can create a list that "skips" numbers.
# Here, my range(2, 20, 2) will give me a list where each number is 2 greater than the previous number.

myList = range(2, 20, 2)
print(list(myList))

# OUTPUT: [2, 4, 6, 8, 10, 12, 14, 16, 18] - Interesting!
# Here's some more --

myList = range(1, 100, 10)
print(list(myList))

# OUTPUT: [1, 11, 21, 31, 41, 51, 61, 71, 81, 91]
# My list stops at 91 because the next number in the sequence would be 101, 
# which is greater than or equal to 100, my stopping point.

# Mmmmmmmm, here's two more --

fiveThree = range(5, 15, 3)
print(list(fiveThree))

zeroFive = range(0, 40, 5)
print(list(zeroFive))