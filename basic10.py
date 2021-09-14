# 内包表記　if
l = []
for i in range(1, 31):
    if i % 3 == 0 and '3' in str(i):
        l.append(i)

print(f'作成したリスト : {l}')


l = [i for i in range(1, 101) if i % 3 == 0]
n = [i for i in l if "3" in str(i)]
print(n)


L = [i for i in range(3, 101, 3) if "3" in str(i)]
print(L)
