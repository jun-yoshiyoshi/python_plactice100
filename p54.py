l = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

for i, row in enumerate(l, start=1):
    a, b, c = row
    print(f'{i}行目の値 : {a} {b} {c}')



for m,(a,b,c) in enumerate(l,1):
    print("{}行目の値:{} {} {}".format(m,a,b,c))

リスト、タプル、エニュメレイト