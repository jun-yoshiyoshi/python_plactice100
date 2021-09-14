# 内包表記　リスト
l = []
for i in range(1, 31):
    if i % 3 == 0:
        l.append(i)
print(f'作成したリスト : {l}')


l = [i for i in range(3, 31, 3)]
print(f'作成したリスト : {l}')
