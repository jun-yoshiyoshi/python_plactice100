# set関数　append関数
l = [1, 2, 2, 3, 3, 4, 5]
new_l = list(set(l))
print(f'重複削除したリスト : {new_l}')


L = []
for i in l:
    if i not in L:
        L.append(i)
    else:
        continue
print(f'重複削除したリスト : {L}')

# 未完成のリストを変数にした内包表記はできないのかもしれない。
# 要素が確定していないので、Lリスト内の要素iの、存在も確定できないからか。

l = [1, 1, 2, 2, 3, 4, 4, 4, 5]
b = []
L = [i for i in l if i not in b and not b.append(i)]
print(L)
print(b)
