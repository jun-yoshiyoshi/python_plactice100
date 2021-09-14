# 内包表記　辞書型
d = {}
for i in range(1, 31):
    if i % 3 == 0:
        index = f'{i // 3}番目'
        d[index] = i
print(f'作成したリスト : \n{d}')

l = [i for i in range(1, 51) if i % 3 == 0]
L = [f"{int(i/3)}番目" for i in l]
print(f"作成したリスト:\n{dict(zip(L,l))}")


d = {f'{(k+1)}番目': v for k, v in enumerate(range(3, 101, 3))}
print(f"作成したリスト:\n{d}")
