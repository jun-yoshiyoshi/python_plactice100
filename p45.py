l = [1, 2, 3, 4, 5]
for i in range(0, 10, 2):
    l.insert(i, 'list')
print(f'"list"を追加したリスト : {l}')

//in range(0,10,2):は'list'をinsertする
indexの指定をしている。
対象リスト.insert(位置, 挿入オブジェクト)//