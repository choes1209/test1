# Подсчитать количество букв 'а' в словах
# из списка ['aaabb', 'caca', 'dabc', 'acc', 'abbba']
# и вывести результат в виде списка т.е. вывод - [3, 2, 1, 1, 2]

lst = ['aaabb', 'caca', 'dabc', 'acc', 'abbba']
res = [s.count('a') for s in lst]

print(res)
