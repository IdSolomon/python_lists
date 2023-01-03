# When I want to add multiple items to a list, I can
# use + to combine two lists.

toysSold = ["megatron", "skeletor", "shredder"]
print(toysSold)

# Creating a new variable, toysSold_new, which contains
# both the original items sold and the new items.

toysSold_new = toysSold + ["wolverine", "spawn", "batman"]
print(toysSold_new)

# Creating a new variable by combining several variables with
# their respective lists.

megazord = ["mastodon", "pterodactyl", "triceratops", "saber-toothed tiger", "tyrannosaurus"]
print(megazord)

dragonzord = ["dragonzord"]
print(dragonzord)

titanus = ["titanus"]
print(titanus)

megaUltrazord = megazord + dragonzord + titanus
print(megaUltrazord)