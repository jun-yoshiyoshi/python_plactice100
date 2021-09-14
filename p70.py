keys = ['A', 'B', 'C']
values = [111, 222 ,333]

d = {key:value for key, value in zip(keys, values)}
print(f'作成した辞書 : {d}')

d=dict(zip(keys,values))