print("\033[H\033[J", end="")
# Lesson 2.
list_1 = []    # Пустой список.
list_1 = list()  # f-ция list() также создаёт пустой список.
list_1 = [7, 6, 5 , 4] # Сразу со знач..
print(*list_1)   # Ес хотим без кв-скобок. "* - открывает список и мы просто перебираем какие-л знач.."

count = 1
for i in list_1:
    print(f"{count}-й Элемент равен: {i}.")
    count += 1
print()

print(f"{len(list_1)} - длина списка.")
print(f"{list_1[-2]} - 2-й с конца элемент списка.")

list_1.append(8)
print(*list_1)

list_2 = []
print(list_2)
for i in range(5): # П-менная i б-приним знач.. от 1 до 4.
    list_2.append(i)
    print(list_2)
print()

list_3 = [12, 7, -1, 21, 0]
print(list_3)
print(list_3.pop())   # 0
print(list_3)
print(list_3.pop())   # 21
print(list_3)
print(list_3.pop())   # -1
print(list_3)
print(list_3.pop())   # 7
print(list_3)
print(list_3.pop())   # 12. Также F "pop" возв-т удаляемый элемент.
print(list_3)

list_3 = [12, 7, -1, 21, 0]  # Удалим элемент по указ-индексу.
print(f'{list_3} - list_3.')
print(list_3.pop(2))   # -1.  Арг. в "pop" это индекс удаляемого эл.
print(f'{list_3} - list_3.')

# +добим эл. на нужную поз.
list_4 = [12, 7, -1, 21, 0]
print(list_4.insert(2, 35))  # 1арг - это поз., на кую нуж вставить эл. 2арг - знач., кое приним этот эл.
print(f'{list_4} - list_4.')  # [12, 7, 35, -1, 21, 0]

print(list_4[0:len(list_4):1])
print(list_4[0:len(list_4)-1:1])
print(list_4[::1])
print(list_4[1:3])

# Кортеж - это неизменяемый список.
# Нужен в сл. защиты д.. от изм. (намеренных или сл). Кортеж заним мень места в пам. и раб быстрее списка.

t = ()   # Созд. пустого кортежа.
print(t) # class <'tuple'>
print(type(t))
t = (1)  # - без запятой на конце: int.  (видимо - без зап. и ес толь 1 эл.)
print(t)
print(type(t))
t = (1,)  # - с запятой на конце: кортеж tuple.
print(t)
print(type(t))
v = (14, 11, 1991)  # - в круглых: кортеж tuple.
print(v)
print(type(v))
v = [14, 11, 1991]  # - в квадратных: список list.
print(v)
print(type(v))
v = [14, 11, 1991,]  # - в квадратных: список list. (запятая на конце ничего не изм, это всё равно список).
print(v)
print(type(v))
# в квадратных и с одним эл. выдаст ошибку!

a = 5
b = 5       # Исх запись.
a, b = 5, 5 # Равнозначные записи.
a = b = 5   # Равнозначные записи.

a, b, c = v
print(a, b , c) # выв-ся в 3 отдельные п-менные. Т.е. мы сдел "распаковку" кортежа.
print()
# Словари - неупорядоченные коллекции произвольных объ.. с доступом по ключу.
# (не индекс, а знач. ключа (строка, число)).
dictionary = {}  # Cоздали пустой словарь.
d = dict()       # Cоздали пустой словарь.
d['q'] = 'qwerty'
print(f'{d} - добавили 1й эл. с ключом q и значением qwerty')
d['w'] = 'werty'
print(d)
d['l'] = 'lao'
print(d)
del d ['w']  # Удаление эл. c ключом 'w'.

print(d)     # 1-й способ вывести все ключи и значения.

for i in d:  # Выв только ключи.
    print(i)
    
for(k,v)in d.items():# 2-й способ вывести все ключи и значения.
    print(k, v)
    
for i in d:          # 3-й способ вывести все ключи и значения.
    print(f'{i}: {d[i]}')
    
print(d.items())     # 4-й способ вывести все ключи и значения.
# Выв список (видно по кв-скобкам), где каж-эл. это кортеж (видно по кр-скобкам).

print()
# Множества.    Синтак-ки пишутся также ={}. Но не имеют ключей ":".
# Содержат уникальные неупорядоченные эл.. со знач.. люб-типов.
q = set()   # Cоздали пустое множество.
colors = {'red', 'green', 'blue'}
print(colors)
colors.add('red')     # При +нии ес это знач. уже есть, то ни-не произойдёт.
print(colors)
colors.add('gray')    # +ние нового эл. (в случайное место).
print(colors)
colors.remove('red')  # Удаление эл. Но ес не найдёт такого эл., то выдаст Exeption.
print(colors)
colors.discard('red') # Удаление эл. Но ес не найдёт такого эл., то ни-не произойдёт.
print(colors)
colors.clear()        # Удаление всех эл..
print(colors)

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()          # Полная копи.
u = a.union(b)        # {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b) # {2, 5, 8} - очерёдность не важна.
dl = a.difference(b)  # {1, 3}
dr = b.difference(a)  # {13, 21}
q = a.union(b).difference(a.intersection(b))  # {1, 3, 13, 21}
print(c)
print(u)
print(i)
print(dl)
print(dr)
print(q)

j = frozenset(i)  # Неизменяемое множество.
print(j)
#j[1] = 7  # Выдаст Exeption.

# Генератор списка. "Понимание списка" дословно.  Упрощённый подход к созданию списков,
# кый задей цикл for, а также инструкции if-else для опр. того что в итоге окажется в финальном списке.
# list_5 = [exp for item in iterable]     # синтаксис.
# list_6 = [exp for item in iterable (if conditional)]