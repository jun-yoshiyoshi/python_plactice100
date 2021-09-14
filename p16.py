#　ループ文と数えあげ変数
word = input('文字を入力してください > ')
count = 0

for _ in word:
    count += 1

print(f'{word}の文字数 : {count}')
