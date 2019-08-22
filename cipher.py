import fileinput
from string import ascii_lowercase

banked = False
out = []
answer = []

for line in fileinput.input():
    input = line

for char in input:
    if char.isdigit():
        if not banked and int(char) < 3:
            banked = True
            bankednum = char
            continue
        elif banked:
            check = bankednum + char
            if int(check) < 26:
                out.append(int(check))
                banked = False
for i in out:
    answer.append(ascii_lowercase[i])

print(''.join(answer))