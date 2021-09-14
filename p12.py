#　float型　input関数
h = float(input('身長を入力してください(cm) > ')) / 100
w = float(input('体重を入力してください(kg) > '))

bmi = w / h ** 2
print(f'BMI = {bmi}')
