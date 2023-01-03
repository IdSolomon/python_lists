# I also want to count occurrences of an item in a list.
# If I want to know how many times an element appears in a list,
# I can use the list method called .count() --

marvelHeroes = ["Iron Man", "Spider-Man", "Hulk", "Wolverine", "Iron Man", "Nightcrawler", "Captain America", "Iron Man"]

IronMen = marvelHeroes.count("Iron Man")
print(IronMen)

# OUTPUT: 3
# Apparently there are 3 Iron Men.....

# I can also use .count() to count element appearances in a two-dimensional list.

mainCharacters = [
    ["Potter", "Gryffindor"], 
    ["Weasley", "Gryffindor"],
    ["Hermione", "Gryffindor"],
    ["Potter", "Gryffindor"],
    ["Ginny", "Gryffindor"],
    ["Draco", "Slytherin"],
    ["Potter", "Gryffindor"],
    ["Longbottom", "Gryffindor"],
    ["Lovegood", "Ravenclaw"],
    ["Potter", "Gryffindor"]
]

numOfPairs = mainCharacters.count(["Potter", "Gryffindor"])
print(numOfPairs)

# OUTPUT: 4

namesList = [
    "JCVD",
    "Stallone",
    "Leonardo",
    "Leonardo",
    "Megatron",
    "Bugs Bunny",
    "Leonardo",
    "He-Man",
    "Trevor Philips",
    "Leonardo"
]

leonardo = namesList.count("Leonardo")
print(leonardo)

# OUTPUT: 4