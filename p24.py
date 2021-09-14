# len関数
word = input('英単語を入力してください > ')
count = 0

for _ in word:
    count += 1

index = count // 2

if count % 2 == 0:
    word = word[:index] + '@' + word[index:]
else:
    word = word[:index] + '@' + word[index+1:]

print(f'変換した英単語 : {word}')


word = input('英単語を入力してください > ')
l = int(len(word)/2)
word_new = word[:l]+"@"+word[-l:]
print(f'変換した英単語 : {word_new}')
