import random

ls = [random.randint(1, 30) for i in range(20)]
ls = sorted(ls[:10], ) + sorted(ls[10:], reverse=True)
print(ls)
