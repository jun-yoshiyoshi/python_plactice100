# リスト型　for文
l = [1, 5, 3, 2, 4]
max_value = l[0]

for i in l:
    if i > max_value:
        max_value = i

print(f'リスト内の最大値 : {max_value}')
