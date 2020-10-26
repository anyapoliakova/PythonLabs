let1_to_let2 ={
    'a':'0', 'e':'1', 'i':'2', 'o':'2', 'u':'3'
}

def encrypt(phrase):
    res = ''
    for letter in phrase[::-1]:
        if letter in let1_to_let2:
            res += let1_to_let2[letter]
        else:
            res += letter
    return res +'aca'

print('encrypt("banana") ->', encrypt("banana"))
print('encrypt("karaca") ->', encrypt("karaca"))
print('encrypt("burak") ->', encrypt("burak"))
print('encrypt("alpaca") ->', encrypt("alpaca"))
