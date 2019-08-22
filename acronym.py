import fileinput


for line in fileinput.input():
    words = line.split()
acronym = []
for word in words:
    if word[0].isupper():
        acronym.append(word[0])

print(''.join(acronym))