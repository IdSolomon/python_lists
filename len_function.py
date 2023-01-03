# Sometimes, I don't like counting the number of items in a list if it's too long.
# This is usually called its length, so I use a built-in function called len().
# len() helps me get the number of elements in a list --

myList = [1, 2, 3, 4, 5]
print(len(myList))

# OUTPUT: 5
# So, according to my terminal, there are 5 items in myList. Nice!

# I got another list, this time the list contains some numbers, a float, booleans, and familiar strings
# from the 80s and 90s variety.

anotherList = [7, 13, 94.5, True, False, True, 
    "JCVD", 
    "Stallone", 
    "Snipes", 
    "Schwarzenegger", 
    "Lundgren", 
    "Norris",
    "Seagal"
]
print(len(anotherList))

# OUTPUT: 13
# Here's a BIG range.

bigRange = range(2, 3000, 100)

bigRangeLength = len(bigRange)
print(bigRangeLength)

# OUTPUT: 30