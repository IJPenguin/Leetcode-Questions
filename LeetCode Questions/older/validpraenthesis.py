# s = "){"
s = "()[]{}"
dict = {"(": ")", "[": "]", "{": "}"}
stack = []
if len(s) == 1:
    print (False)
    
for char in s:
    print(char)
    if char in dict.keys():
        stack.append(char)
        print(stack)
    elif char in dict.values():
        if len(stack) == 0:
            print(False)
            break
        if dict[stack[-1]] != char:
            print (False)
            print(stack)
            break
        else:
            stack.pop(len(stack)-1)
            print(stack)

if len(stack) != 0:
    print (False)
else: 
    print (True)

