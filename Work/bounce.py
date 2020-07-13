# bounce.py
#
# Exercise 1.5

bounces = 10
height = 100

for i in range(1, bounces + 1):
    height = 0.6 * height
    print(f"{i}: {round(height, 4)}")
