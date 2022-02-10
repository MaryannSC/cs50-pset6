with open("fox.txt", "r") as file:
    seq = file.read()

loc = 0
count = 1
maxCount = 0
foundLoc = seq.find("THE", loc)

while (foundLoc != -1):
    print(f"found THE at location {foundLoc}")
    loc = foundLoc + 1
    foundLoc = seq.find("THE", loc)
    # check if sequential
    if foundLoc == loc - 1 + len("THE"):
        count += 1
        if count > maxCount:
            maxCount = count
    else:  # not sequential
        count = 1

print(f"Max count = {maxCount}")


