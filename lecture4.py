dct = dict(zip(('key1', 'key2'), ('val1', 'val2')))
dct1 = dct.copy()
del dct1['key1']
print(dct, dct1)

# Есть словарь dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}
# Составить из него новый словарь, содержащий только те элементы, у которых значение больше или равно 3.
dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}
dict_new = {}
for k, v in dict.items():
    if v >= 3:
        dict_new[k] = v
print(dict_new)
