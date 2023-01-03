# Prepare to have your mind blown --
# Aside from list items being numbers or strings, lists can contain other lists!
# These are called two-dimensional (2D) lists.

# Previously, my team ordered sustenance through Grubhub.
# No one remembered ordering a California Roll, so I removed it.
# Now, for efficiency-sake, I will create a 2D list with my team's name and order number.

grubhubOrder = [
    ["Jen", 4], 
    ["Alex", 7],
    ["Monica", 2],
    ["Tyler", 12],
    ["Roma", 2],
    ["Me", 1]
]

# I had a last minute order, so I will try and append it.

grubhubOrder.append(["Vikky", 5])
print(grubhubOrder)

# OUTPUT: [['Jen', 4], ['Alex', 7], ['Monica', 2], ['Tyler', 12], ['Roma', 2], ['Me', 1], ['Vikky', 5]]
# Convenience is king!