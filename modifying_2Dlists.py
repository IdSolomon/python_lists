# I'm once again going back to my team's costly Grubhub sushi order!
# I can now modify the order since one member of my team, Roma, decided to change her mind.
# She wants a different order. A different sushi order.

grubhubOrder = [
    ["Jen", 4], 
    ["Alex", 7],
    ["Monica", 2],
    ["Tyler", 12],
    ["Roma", 2],
    ["Me", 1],
    ["Vikky", 5]
]

# Roma is now more interested in order number 1. The same order as Me.
# So, to change a value in a two-dimensional list, I have to reassign the value using the specific index.
# The list of Roma is at index 4. Her order is at index 1 --

grubhubOrder[4][1] = 1
print(grubhubOrder)

# OUTPUT: [['Jen', 4], ['Alex', 7], ['Monica', 2], ['Tyler', 12], ['Roma', 1], ['Me', 1], ['Vikky', 5]]
# Rejoice!! Roma now has the same order number as Me.

# Switching things up a bit, we're now at school. But this isn't your ordinary school.
# Recent peculiar events have led up to a class change as a new group of kids emerge
# and join the original class.

OGClass = [
    ["Potter", "Gryffindor"], 
    ["Weasley", "Gryffindor"],
    ["Hermione", "Gryffindor"],
    ["Ginny", "Gryffindor"],
    ["Draco", "Slytherin"],
    ["Longbottom", "Gryffindor"],
    ["Lovegood", "Ravenclaw"]
]

NewClass = [
    ["Chunk", "Hufflepuff"], 
    ["Mikey", "Gryffindor"],
    ["Data", "Ravenclaw"],
    ["Mouth", "Gryffindor"],
    ["J_Connor", "Gryffindor"],
    ["S_Tanner", "Hufflepuff"],
    ["A_Banks", "Ravenclaw"]
]

combinedClass = OGClass + NewClass
print(combinedClass)

# OUTPUT: [
#   ['Potter', 'Gryffindor'], 
#   ['Weasley', 'Gryffindor'], 
#   ['Hermione', 'Gryffindor'], 
#   ['Ginny', 'Gryffindor'], 
#   ['Draco', 'Slytherin'], 
#   ['Longbottom', 'Gryffindor'], 
#   ['Lovegood', 'Ravenclaw'], 
#   ['Chunk', 'Hufflepuff'], 
#   ['Mikey', 'Gryffindor'], 
#   ['Data', 'Ravenclaw'], 
#   ['Mouth', 'Gryffindor'], 
#   ['J_Connor', 'Gryffindor'], 
#   ['S_Tanner', 'Hufflepuff'], 
#   ['A_Banks', 'Ravenclaw']
# ]
# Fascinating!