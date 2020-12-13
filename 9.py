def time_adjust(t_str, hrs, mins, sec):
    (h, m, s) = list(map(int, t_str.split(':')))
    s += sec
    m += mins + (s // 60)
    h += hrs + (m // 60)
    (s, m, h) = (s % 60, m % 60, h % 24)
    return '{:02d}:{:02d}:{:02d}'.format(h, m, s)


print(time_adjust('01:00:00', 1, 30, 10))
print(time_adjust('18:22:30', 4, 60, 30))
print(time_adjust('00:00:00', 72, 120, 120))
