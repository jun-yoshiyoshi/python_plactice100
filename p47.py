l = [1, 3, 2, 3, 4, 6, 5, 8, 7]
for i, v in enumerate(l):
    if i % 3 == 0 and v % 3 == 0:
        l.pop(i)
print(f'削除後のリスト : {l}')

# あまり良くない例
# もしリストに9が追加されたら9w削除できなくなる
# 新しく生成するのが良い

l=[i for n,i in enumerate(l) if i%3>0 or n%3>0 ]
print(l)