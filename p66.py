d1 = {'A': 111, 'B': 222, 'C': 333}
d2 = {'D': 444, 'E': 555}
d3 = {'F': 666}

new_d = {}

for d in [d1, d2, d3]:
    new_d.update(d)

print(f'連結した辞書 : {new_d}')