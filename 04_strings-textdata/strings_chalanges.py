"""
- Create two variables both representing something you want for your birthday

- Create a new variable called 'birthday_gifts_phrase' stating for your birthday
you want the two variables. Make sure you concatenate the two items into your phrase.

- Print the birthday_gifts_phrase in capital letters using the correct method.
"""

# There  are 3 ways to handle this
# 1
item_one = "Bike"
item_two = "Cell Phone"
birthday_gits_phrase = f'For my birthday I want {item_one} amd {item_two}'
print(birthday_gits_phrase)

# 2
birthday_gits_phrase_another_way = 'For my birthday I want {item_one} and {item_two} amd {item_two}'.format(item_one=item_one, item_two=item_two)
print(birthday_gits_phrase_another_way.upper())