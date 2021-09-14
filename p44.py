l = [1, 2, 3, '4', 5]
if any([v for v in l if isinstance(v, str)]):
    print('文字列が入っています。')
else:
    print('文字列は入っていません。')