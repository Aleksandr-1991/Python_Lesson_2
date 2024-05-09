print("\033[H\033[J", end="")
# 2. Добавим условие (только чётные числа).

list_1 = [i for i in range(1, 101) if i%2 == 0]   # [2, 4, 6, ...100]
print(list_1)
print()
# Создаём пары каждому из чисел (кортежи).
list_2 = [(i, i) for i in range(1, 101) if i%2 == 0]
print(list_2)
print()
# Так же мож умножать, делить, приб, выч.  Например, умнож на 2:
list_3 = [i*2 for i in range(1, 101) if i%2 == 0]
print(list_3)
print()