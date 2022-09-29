# Дана последовательность чисел. 
# Получить список уникальных элементов заданной последовательности.
# ​Пример:​[1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]​

from random import randint

a = [int(s) for s in input().split()]
for i in range(len(a)):
    for j in range(len(a)):
        if i != j and a[i] == a[j]:
            break
    else:
        print(a[i], end=' ')
