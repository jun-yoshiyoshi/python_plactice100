# データ型　int型 format関数
i = int(input('好きな整数を入力してください > '))
print(f'{i}の二乗値 : {i**2}')
# print('{i}の二乗値 : {i**2}'.format)　エラーになります
print("{}の二乗値 : {}".format(i, i**2))
