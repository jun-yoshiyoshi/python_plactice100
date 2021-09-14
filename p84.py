l = [1, 0, [], (2, 3), 'AA', '', False, ''*3]
is_true_count = sum([bool(v) for v in l])
print(f'Trueの数 : {is_true_count}')