# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
s = int(input('Ввведите количество журавликов S: '))
if s%6 == 0:
    p = c = s*(1/6)
    k = s*(2/3)
    print(int(p), int(k), int(c))
else:
    print('Введите число журавликов, кратное 6')