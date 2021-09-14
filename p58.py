t = (1, [2, 3], '4', (5, 6, 7), None, (9, 10))
t_to_tuple = []
for v in t:
    if isinstance(v, tuple):
        t_to_tuple.append(v)
    elif isinstance(v, list):
        t_to_tuple.append(tuple(v))
    else:
        t_to_tuple.append((v, ))

print(f'変換したタプル : {tuple(t_to_tuple)}')