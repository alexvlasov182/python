"""
For Loops Assignment

- Create a list variable that holds the digits 1 -> 8
- Iterate through the list using a for loop
- Print all elements into the console, unless an element is 3 or 7
"""

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in number_list:
    if number == 3 or number == 7:
        continue
    print(number)