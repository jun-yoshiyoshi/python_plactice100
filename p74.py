d = {'B': 222, 'A': 111, 'D': 333, 'C': 444}
sort_by_value = dict(sorted(d.items(), key=lambda x: x[1]))
print(f'Valueでソートした辞書 : {sort_by_value}')


items()は辞書データをタプル型で取り出す

key=lambda関数は引数xのとき、xの[n]を戻り値として返す。

戻り値はタプル型が並んだデータなので、辞書型に成形しなおす。