def char_range(c1, c2):
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)

def super_reduced_string(text):
    res = text
    found = True
    while found:
        found = False
        for c in char_range('a', 'z'):
            if c * 2 in res:
                found = True
                res = res.replace(c * 2, '')
    return res if res != '' else 'Empty String'

print(super_reduced_string("cccxllyyy"))
print(super_reduced_string("aa"))
print(super_reduced_string("baab"))
print(super_reduced_string("fghiiijkllmnnno"))
print(super_reduced_string("chklssstt"))

