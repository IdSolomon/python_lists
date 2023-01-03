# I'm going back to my team's Grubhub ordering list, which proved to be real costly - sushi is expensive!
# I can access the list by going into the sublist's index, and then accessing the other index of said sublist.

grubhubOrder = [
    ["Jen", 4], 
    ["Alex", 7],
    ["Monica", 2],
    ["Tyler", 12],
    ["Roma", 2],
    ["Me", 1],
    ["Vikky", 5]
]

jenOrder = grubhubOrder[0][1]
print(jenOrder)

# OUTPUT: 4

vikkyOrder = grubhubOrder[-1][-1]
print(vikkyOrder)

# OUTPUT: 5