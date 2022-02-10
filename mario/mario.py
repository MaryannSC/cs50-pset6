# mario.py creates half pyramid using hashes (#)
# pyramid is aligned to the bottom left corner
# with no extra spaces at the end of each line

from cs50 import get_int

# get integer input, verify between 1 and 8 inclusive
while True:
    height = get_int("Height: ")
    if height > 0 and height < 9:
        break

# create half pyramid
for i in range(height):
    for j in range(height - 1 - i):
        print(" ", end="")
    for k in range(i + 1):
        print("#", end="")
    print()