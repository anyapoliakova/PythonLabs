def staircase(n):
    width = abs(n)
    line = lambda w: ('#' * w).rjust(width, '_')
    lengths = range(1, width + 1) if n > 0 else range(width, 0, -1)
    return '\n'.join([line(w) for w in lengths])

print(staircase(7))
print(staircase(-8))
