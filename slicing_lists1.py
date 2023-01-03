# Sometimes, when I want something, I don't want the whole thing.
# I want a portion of it. This includes a list.
# Dividing a list in such a manner is referred to as slicing.

movies = ["Inception", "The Matrix", "Die Hard", "Demolition Man", "Rocky", "Bloodsport", "Enter The Dragon"]

# By following this syntax, I can make my selection - movies[start:end]

slicedMovies = movies[2:4]
print(slicedMovies)

# OUTPUT: ['Die Hard', 'Demolition Man']
# Index 2 is selected, but index 4 specifically is not.

marvelVillains = ["Dr. Doom", "Red Hulk", "Venom", "Juggernaut", "Magneto", "Red Skull", "Iron Monger"]

slicedVillains = marvelVillains[3:4]
print(slicedVillains)

# OUTPUT: ["Juggernaut"]