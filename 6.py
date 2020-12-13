import re

pattern = r'^(?!.*(.).*\1)\d+$'
result = bool(re.match(pattern, '112233'))

print(bool(re.match(pattern, "123")))
print(bool(re.match(pattern, "112233")))
print(bool(re.match(pattern, "1025")))
