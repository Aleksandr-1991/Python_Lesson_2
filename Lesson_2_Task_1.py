print("\033[H\033[J", end="")
# Создать список из чётных чисел в диапазоне 1 до 100.
list_1 = []
for i in range(2, 100, 2):
    list_1.append(i)
print(list_1)

# эту же f мож записать так:
list_1 = [i for i in range(2, 100, 2)]
print(list_1)