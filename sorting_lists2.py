# A second way of sorting a list in Python is to use the built-in function sorted().
# The sorted() function is different from the .sort() method in two ways --
# 1. It comes before a list, instead of after as all built-in functions do.
# 2. It generates a new list rather than modifying the one that already exists.

namesOnList = [
    "Will Smith", 
    "Carlton Banks", 
    "Hilary Banks", 
    "Ashley Banks", 
    "Philip Banks", 
    "Vivian Banks", 
    "Geoffrey Butler"
]

# Using sorted(), I can create a new list, called characterNames --

characterNames = sorted(namesOnList)
print(characterNames)

# OUTPUT: [
#   'Ashley Banks', 
#   'Carlton Banks', 
#   'Geoffrey Butler', 
#   'Hilary Banks', 
#   'Philip Banks', 
#   'Vivian Banks', 
#   'Will Smith'
# ]

# Note: Using sorted did not change namesOnList --

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

games = ["Grand Theft Auto", "Doom Eternal", "Watch Dogs", "Assassin's Creed", "SimCity4000"]

sortedGames = sorted(games)
print(games)
print(sortedGames)

# OUTPUT: games = ['Grand Theft Auto', 'Doom Eternal', 'Watch Dogs', "Assassin's Creed", 'SimCity4000']
# OUTPUT: sortedGames = ["Assassin's Creed", 'Doom Eternal', 'Grand Theft Auto', 'SimCity4000', 'Watch Dogs']