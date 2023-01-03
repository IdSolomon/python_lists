# The Python list method .insert() allows me to add an element to a specific index in a list.
# The method takes in two inputs --
# 1. The index I want to insert into.
# 2. The element I want to insert at the specified index.

nightclubLine = ["Embra", "Karla", "Jonn", "Carlo", "Maxi", "Havier"]

nightclubLine.insert(0, "Eddy")
print(nightclubLine)

# OUTPUT: ['Eddy', 'Embra', 'Karla', 'Jonn', 'Carlo', 'Maxi', 'Havier']
# Here we have a line outside one of the hottest nightclubs in the city.
# A girl, Embra, happens to be saving a spot for a gentleman. She is at the front of the line.
# To everyone's anger and frustration, this gentleman, Eddy, is able to skip to the front of the line
# when I use the .insert() method. #sorrynotsorry

bankLine = ["Joshua", "Frank", "Charlie", "Rand", "Sarah"]

bankLine.insert(2, "Thomas")
print(bankLine)

# OUTPUT: ['Joshua', 'Frank', 'Thomas', 'Charlie', 'Rand', 'Sarah']
# Here Thomas moves into the third position of the line. Or at the 2nd index.