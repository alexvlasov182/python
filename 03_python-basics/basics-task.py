"""
- Create a variable "bank_amount"
assign it to the value of 100

- Create three more variables:
    item_one = 25
    item_two = 30
    item_three = 15

- Subtract each item from bank_amount.

- print how much is left in the bank account
at the end

- Write a comment at the top explaining
what your application does.
"""
"""
Subtracts each item from bank_amount
and prints the remaining bank_amount
"""
bank_amount = 100

item_one = 25
item_two = 30
item_three = 15

bank_amount = bank_amount - item_one
bank_amount -= item_two
bank_amount -= item_three

print(bank_amount)
