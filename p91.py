import random

d = {
    0: 'グー',
    1: 'チョキ',
    2: 'パー'
}
options = tuple(d.keys())
compute_hand = random.choice(options)

my_hand = 99
while my_hand not in options:
    my_hand = input('自分が出す手を入力してください(整数 : 0, 1, 2) > ')
    try:
        my_hand = int(my_hand)
    except:
        print('整数の0, 1, 2を入力してください')

print(f'コンピューターが選んだ数字 : {compute_hand}, 型 : {type(my_hand)}')
print(f'自分が選んだ数字 : {my_hand}, 型 : {type(my_hand)}')

