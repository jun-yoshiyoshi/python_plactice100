l = [1, 'aaa', 2, 'bbb', 'ccc',  3, 'ddd', 4]
int_l = sorted([v for v in l if isinstance(v, int)])
str_l = sorted([v for v in l if isinstance(v, str)])
print(f'ソートしたリスト : {int_l + str_l}')
