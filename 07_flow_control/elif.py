"""
Elif statement

if condition1:
  # block of code to be executed if condition1 is true
    # code to execute if condition1 is True
elif condition2:
  # block of code to be executed if condition1 is false and condition2 is true
    # code to execute if condition2 is True
else:
  # block of code to be executed if condition1 is false and condition2 is false
    # code to execute if both condition1 and condition2 are False

"""

HOUR = 15

if HOUR < 15:
    print("Good morning")
elif HOUR < 20:
    print("Good afternoon")
else:
    print("Good night")
