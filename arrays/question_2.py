# Question
"""
You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']
Using this find out,

1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
"""

# Solution

heros = ["spider man", "thor", "hulk", "iron man", "captain america"]

# Question 1
print(len(heros))

# Question 2
heros.append("black panther")
print(heros)

# Question 3
heros.remove("black panther")
heros.insert(3, "black panther")
print(heros)

# Question 4
heros[1:3] = ["doctor strange"]
print(heros)

# Question 5
heros.sort()
print(heros)
