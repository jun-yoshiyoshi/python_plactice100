l1 = [4, 6, 9, 2]
l2 = [3, 5, 7]
l3 = [1, 9, 7]

l = [l1, l2, l3]
sorted_l = sorted(l, key=lambda v: sum(v) / len(v), reverse=True)

print(f'平均値が最も高いリスト : {sorted_l[0]}')

l4=sorted([l1,l2,l3], key=lambda v:sum(v)/len(v))
print(f'平均値が最も高いリスト : {l4[-1]}')