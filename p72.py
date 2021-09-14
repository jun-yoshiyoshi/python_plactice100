l = ['B', 'C', 'D', 'A']
d = {'A': 111, 'B': 222, 'C': 333}
for key in l:
    print(f'{key}に対応するValue : {d.get(key)}')