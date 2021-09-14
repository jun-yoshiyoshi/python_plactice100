# count関数:文字列中の文字数を数える
word = input('文字列を入力してください > ')

d = {}
for s in word:
    if s in d.keys():
        d[s] += 1
    else:
        d[s] = 1
print(d)

word = input("文字列を入力してください:")
d = {k: word.count(k) for k in word}
print(d)
