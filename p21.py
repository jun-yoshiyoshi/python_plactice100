# isupper関数　islower関数
word = input('文字列を入力してください > ')

if word[0].islower():
    word = word[0].upper() + word[1:]
elif word[0].isupper():
    word = word*2

print(f'変換後の文字列 : {word}')


word = input('文字列を入力してください > ')
print(f"{word[0].upper()}{word[1:]}") if word[0].islower() else word*2
