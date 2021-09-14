# split関数　append関数

sentence1 = input('1つ目の英文を入力してください > ')
sentence2 = input('2つ目の英文を入力してください > ')

sentence1 = sentence1.split()
sentence2 = sentence2.split()

r = []
for word in sentence1:
    if word in sentence2 and not word in r:
        r.append(word)

print(f'重複する英単語 : {r}')

sentence_a = input("文字列aを入力してください＞").split()
sentence_b = input("文字列bを入力してください＞").split()
c = [i for i in sentence_a if i in sentence_b and i not in c]
print(f"重複する文字列：{c}")

sentence_a = input("文字列aを入力してください＞").split()
sentence_b = input("文字列bを入力してください＞").split()
print(f"重複する文字列：{set(sentence__a)&set(sentence_b)}")
