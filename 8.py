def super_reduced_string(text):
    found = True
    res = text
    while found:
        (res, found) = remove(res)
    return res if len(res) > 0 else 'Empty String'

def remove(text):
    res = ''
    found = False
    i = 0
    while i < len(text)-1:
        if text[i] == text[i+1]:
            i += 2
            found = True
        else:
            res += text[i]
            i += 1
    if len(text) >= 2 and text[len(text) -1] != text[len(text) - 2]:
        res += text[len(text) - 1]
    return (res, found)


# print(super_reduced_string('aaabb'))
line = 'abbcd'
pairs = [(line[i], line[i+1]) for i in range(0, len(line) - 1)]
filtered = list(filter(lambda p: p[0] != p[1], pairs))
print(''.join([p[0] for p in filtered]) + filtered[-1][1])
