# Sometimes, I can be a real perfectionist.
# So using the .sort() method makes sense!
# I love sorting my lists in either numerical or alphabetical order.

namesOnList = [
    "Will Smith", 
    "Carlton Banks", 
    "Hilary Banks", 
    "Ashley Banks", 
    "Philip Banks", 
    "Vivian Banks", 
    "Geoffrey Butler"
]

namesOnList.sort()
print(namesOnList)

# OUTPUT: [
#   'Ashley Banks', 
#   'Carlton Banks', 
#   'Geoffrey Butler', 
#   'Hilary Banks', 
#   'Philip Banks', 
#   'Vivian Banks', 
#   'Will Smith'
# ]

# .sort() also provides me the option to go in reverse --

namesOnList.sort(reverse=True)
print(namesOnList)

# OUTPUT: [
#   'Will Smith', 
#   'Vivian Banks', 
#   'Philip Banks', 
#   'Hilary Banks', 
#   'Geoffrey Butler', 
#   'Carlton Banks', 
#   'Ashley Banks'
# ]