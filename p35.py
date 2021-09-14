l = ['1', 2, '3', 4.0, '5', 6, '7', 8.0, '9', 10]

new_l = []
for v in l:
    if isinstance(v, int):
        new_l.append(v)

print(f'整数型に絞り込んだリスト : {new_l}')



L=[i for i in l if isinstance(i,int)]
print(L)
