l = [1, 2, None, False, '3', '4', None, True]
is_true_or_none = len([v for v in l if v is True or v is None])

print(f'TrueとNoneの数 : {is_true_or_none}')