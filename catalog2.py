# Показать список ['aaabb', 'caca', 'dabc', 'acc', 'abbba']
# в виде строки, где каждое значение через запятую,
# показывать только слова где встречается буква 'с'.


lst = ['aaabb', 'caca', 'dabc', 'acc', 'abbba']
res = ','.join(i for i in lst if i.find('c')!=-1)
print(res)
