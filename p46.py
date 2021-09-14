l = ['Python1', 'Java1', 1, 'Python2', 'Java2', 2]
for v in l:
    if 'Python' in str(v):
        l.remove(v)
print(f'文字列"Python"を削除したリスト : {l}')


l=[i for i in l if "Python" not in str(i)]
print(l)