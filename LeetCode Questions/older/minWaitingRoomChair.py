# s = "EEEEEEE"
s = "ELELEEL"

fill_chair = 0
empty_chair = 0
for person in s:
    if person == "E":
        if empty_chair:
            empty_chair -= 1
            fill_chair += 1
        else:
            fill_chair += 1
    else:
        fill_chair -= 1
        empty_chair += 1
print(fill_chair + empty_chair)
