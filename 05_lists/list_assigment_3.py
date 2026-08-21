"""
- Create a list variable that holds 5 colors
red
blue
green
pink
purple

- Delete the 0 index
- Delete the element with the value purple
- Add an element with the value white at the end of the list
"""
colors = ['red', 'blue', 'green', 'pink', 'purple']
colors.pop(0)
colors.remove('purple')
colors.append('white')
print(colors)