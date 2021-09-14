# abs関数
a = int(input('1つ目の整数を入力してください > '))
b = int(input('2つ目の整数を入力してください > '))

r = a - b
r = -r if r < 0 else r
print(f'計算結果 : {r}')


a = int(input("一つ目の整数を入力してください＞"))
b = int(input("二つ目の整数を入力してください＞"))
c = abs(a-b)
print(f"計算結果:{c}")

c = a-b
if c < 0:
    c *= (-1)
print(f"計算結果:{c}")

input_a = input("一つ目の整数を入力してください＞")
input_b = input("二つ目の整数を入力してください＞")
print(f"計算結果：{abs(int(input_a)-int(input_b))}")
