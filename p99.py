l = ['アメリカ', 'カナダ', 'スイス', 'メキシコ', 'セントルシア', 'タイ']
sa_l = ['サ', 'シ', 'ス', 'セ', 'ソ']

print('サ行を含む単語 :')
for word in l:
    for sa in sa_l:
        if sa in word:
            print(word)
            break