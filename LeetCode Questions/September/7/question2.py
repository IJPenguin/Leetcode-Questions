s1 = "A str ing A"
s2 = "Astring B"

val1 = 0
val2 = 0

for char in s1:
    if char == " ":
        val1 += 1

for char in s2:
    if char == " ":
        val2 += 1
s = abs(val1 - val2)
print(f"Even{s}" if s % 2 == 0 else f"Odd{s}")
