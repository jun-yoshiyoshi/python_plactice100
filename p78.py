d = {'B': 222, 'A': 111, 'D': 444, 'C': 333}
key_to_get_min_value = min(d.keys(), key=lambda k: d[k])
print(f'最小のValueを持つKey : {key_to_get_min_value}')