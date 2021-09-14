# list関数 set関数　&

l1 = ['Python', 'Ruby', 'PHP', 'JavaScript']
l2 = ['Java', 'Ruby', 'Golang', 'Python', 'TypeScript']

new_l = []
for word1 in l1:
    for word2 in l2:
        if word1 == word2 and word1 not in new_l:
            new_l.append(word1)

print(f'共通する値を格納したリスト : {new_l}')

L = list(set(l1) & set(l2))
print(f"共通する値を格納したリスト:{L}")
