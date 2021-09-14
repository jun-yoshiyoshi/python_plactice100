t = (1, '2', 3, '4', 5)
str_t = (str(v) for v in t)
converted_int = int(''.join(str_t))
print(f'変換後の数値 : {converted_int}')

一度strのリスト型に変換するのがみそ。
intでは''.joinできない。


t =(1, '2', 3, '4', 5, '6', 7, '8', 9)
a=(str(i) for i in t)
a=''.join(a)
a=int(a)
print(f"{a}")