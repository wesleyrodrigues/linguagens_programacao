# listas
in del

lista = [1, 2, 1, 3]
lista2 = ["um", "dois", "um", "um"]

len(lista)                # 4
list(lista2).count("um")  # 3
lista.append(4)           # [1, 2, 1, 3, 4]
lista.count(1)            # 2
lista.pop()               # 4 # remove último item da lista
lista.sort()              # ordena lista # [1, 1, 2, 3]
lista.sort(reverse=True)  # ordena lista # [3, 2, 1, 1]
lista.remove(1)           # [3, 2, 1]
lista.reverse()           # [1, 2, 3] reverte a lista
lista.index(1)            # 0 retorna index do valor passado
lista.insert(0, 10)       # [10, 1, 2, 3] add um número na posição indicada
lista.clear()             # [] apaga todos itens da lista
lista.copy()              # [10, 1, 2, 3] copia a lista

list.extend() # lista.extend(
list.mro()

all([True, False])                  # False
any([True, False])                  # True
sum([1, 2, 3])                      # 6
tuple([1, 2, 3])                    # (1, 2, 3)
list((1, 2, 3))                     # [1, 2, 3]
max([1, 5, 2, 9, 3, 4])             # 9  # Maior valor de uma lista
min([1, 5, 2, 9, 3, 4])             # 1  # Menor valor de uma lista
sorted([2, 3, 1])                   # [1, 2, 3]
sorted([2, 3, 1], reverse = True)   # [3, 2, 1]

enum = enumerate([1, 2, 3])         # <enumerate object at 0x7f09352221f8>
list(enum)                          # [(0, 1), (1, 2), (2, 3)]

rev = reversed([1, 3, 2])           # <list_reverseiterator object at 0x7f82a1f15da0>
list(rev)                           # [2, 3, 1]

z = zip([1, 2, 3], [4, 5, 6])      # <zip object at 0x7f0935219b08>
list(z)                            # [(1, 4), (2, 5), (3, 6)]

mapa = map(float, [1, 2, 3, 4])   # <map object at 0x7f06818bef98>
list(mapa)                        # [1.0, 2.0, 3.0, 4.0]

rang = range(0, 10)               # range(0, 10)
list(rang)                        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# collections adicionar depois 

##################################################################
# Dicionário
##################################################################

d = {"key1": 1, "key2": "value2", "key3": [1, 2]}   # Dicionário

d.items()         # dict_items([('key1', 1), ('key2', 'value2'), ('key3', [1, 2])])
list(d.items())   # [('key1', 1), ('key2', 'value2'), ('key3', [1, 2])]
d.values()        # dict_values([1, 'value2', [1, 2]])
list(d.values())  # [1, 'value2', [1, 2]]
d.pop("key1")     # 1
d.keys()          # dict_keys(['key2', 'key3'])

dict.clear() # dic.clear(
dict.get() # dic.get(
dict.mro()
dict.setdefault() # dic.setdefault(
dict.copy()  # dic.copy(
dict.update() # dic.update(
dict.fromkeys()  # dic.fromkeys(
dict.popitem()   # dic.popitem(

# Edições de um dicionário

d[key1]

##################################################################################
# new
##################################################################################
