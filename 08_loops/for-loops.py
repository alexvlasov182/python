"""
For loops: Iteration!
"""

number_list = [1, 2, 3, 4, 5]
for x in number_list:
    print(x)

for y in range(1, 6):
    print(y)

sum_of_loop = 0
for j in range(3, 6):
    sum_of_loop += j
    print("Sum of loop:", sum_of_loop)

    # 0 + 3 = 3
    # 3 + 4 = 7
    # 7 + 5 = 12

co_workers = ["Alice", "Bob", "Charlie"]
for co_worker in co_workers:
    if co_worker == "Bob":
        print(f"Hello, {co_worker}!")
