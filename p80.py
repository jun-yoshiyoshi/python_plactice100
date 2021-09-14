d = {'B': 222, 'A': 111, 'D': 444, 'C': 333}
new_d = d.copy()
for k, v in d.items():
    if v % 2 != 0:
        del new_d[k]

print(f'奇数を削除した辞書 : {new_d}')

copyメソッドを使わないとnew_dがループする。