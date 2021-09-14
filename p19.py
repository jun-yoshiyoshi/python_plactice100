# replace関数　translate関数　maketrans関数

vowels = ['a', 'i', 'u', 'e', 'o']

word = input('文字列を入力してください > ')

new_word = ''
for s in word:
    if s in vowels:
        continue
    new_word += s

print(f'作成した文字列 : {new_word}')


word = input('文字列を入力してください > ')
new_word = word.replace("a", "").replace("i", "").replace("u", "").replace("e", "").replace("o", "")
print(f'作成した文字列:{new_word}')

s = input("文字を入力してください＞")
print(f"作成した文字列:{s.translate(str.maketrans({'a':'','i': '','u': '','e': '','o': ''}))}")
