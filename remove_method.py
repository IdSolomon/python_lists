# I can remove elements in a list using the .remove() Python method.

groceryLine = ["Michael", "Anne", "Jason", "Brandy"]

groceryLine.remove("Michael")
print(groceryLine)

# OUTPUT: ["Anne", "Jason", "Brandy"]
# As you can see here, I removed Michael from the groceryLine.....
# because he couldn't make up his mind between purchasing either Catsup or Ketchup.

# I can also use .remove() on a list that has duplicate elements.
# However, only the first instance of the matching element is removed. Observe --

groceryLine = ["Sarah", "Sherman", "David", "Sarah", "Yoast"]

groceryLine.remove("Sarah")
print(groceryLine)

# OUTPUT: ["Sherman", "David", "Sarah", "Yoast"]
# BEHOLD! There were two Sarah's, now there's only one. The first Sarah in the list is gone.

# One more example --

grubHubOrder = ["Tempura Shrimp Roll", "California Roll", "Salmon with Avocado Roll", "Eel Roll"]

grubHubOrder.remove("California Roll")
print(grubHubOrder)

# OUTPUT: ["Tempura Shrimp Roll", "Salmon with Avocado Roll", "Eel Roll"]