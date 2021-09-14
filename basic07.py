# if,elif,else fizzbuzz ワンライナー
for i in range(1, 31):
    if i % 15 == 0:
        print('fizzbuzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)

for i in range(1, 51):
    print("Fizz"*(i % 3 < 1)+"Buzz"*(i % 5 < 1) or i)
