telephone_numbers = [
    '080-1203-4455',
    '090-9372-9682',
    '090-3080-4982',
    '080-3917-5918'
]

new_l = [s for s in telephone_numbers if '080' == s[:3]]
print(f'080で始まる電話番号 : {new_l}')