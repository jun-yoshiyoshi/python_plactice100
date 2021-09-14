# sort関数 sorted関数 join関数
word1 = input('1つ目の英単語を入力してください > ')
word2 = input('2つ目の英単語を入力してください > ')
word3 = input('3つ目の英単語を入力してください > ')

words = [word1, word2, word3]

words.sort()
sort_words = ', '.join(words)
print(f'並び替えた英単語 : {sort_words}')


word_a = input("英単語aを入力してください＞")
word_b = input("英単語bを入力してください＞")
word_c = input("英単語cを入力してください＞")
print(f"並び替えた英単語:{sorted([word_a,word_b,word_c])}")

# https: // www.headboost.jp/python-sort/
