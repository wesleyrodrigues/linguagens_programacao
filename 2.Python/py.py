nums = [] 
for i in range(0, int(input())):
    string = input()
    num = int(input())
    for i in string:
        pos = ord(i) - num
        if pos < 65:
            pos = 91 - (65 - pos)
            num += [chr(pos)]
        else:
            chr(pos), end=""
    print()

for i in nums:
