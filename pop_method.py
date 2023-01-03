# Python gives me a method to remove elements at a specific index using a method called .pop().
# The .pop() method takes an optional single input --
# 1. The index for the element you want to remove.

vegetableLasagna = ["carrots", "cucumber", "celery", "banana", "tomatoes", "broccoli"]

removeFruit = vegetableLasagna.pop(3)
print(removeFruit)

# OUTPUT: banana
# The method can be called without a specific index.
# However, our vegetable lasagna wouldn't suffice if a fruit was a part of our ingredient.
# Yes, the debate if a tomatoe is a fruit or a vegetable rages on. So, therefore --

removeFruit = vegetableLasagna.pop(3)
print(removeFruit)

# OUTPUT: tomatoes

print(vegetableLasagna)

# OUTPUT: ['carrots', 'cucumber', 'celery', 'broccoli']
# SUCCESS!! Our vegetable lasagna is complete. Hopefully it's a delight.