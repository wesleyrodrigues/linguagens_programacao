# listas
in del

lista = [1, 2, 3]

list.append() # lista.append()
list.count() # lista.count(
list.insert() # lista.insert(
list.remove() # lista.remove( 
list.clear() # lista.clear(
list.extend() # lista.extend(
list.mro()
list.reverse() # lista.reverse(
list.copy() # lista.copy(
list.index() # lista.index(
list.pop() # lista.pop(
list.sort() # lista.sort(    

all([True, False])                  # False
any([True, False])                  # True
sum([1, 2, 3])                      # 6
tuple([1, 2, 3])                    # (1, 2, 3)
list((1, 2, 3))                     # [1, 2, 3]
max([1, 5, 2, 9, 3, 4])             # 9  # Maior valor de uma lista
min([1, 5, 2, 9, 3, 4])             # 1  # Menor valor de uma lista
sorted([2, 3, 1])                   # [1, 2, 3]
sorted([2, 3, 1], reverse = False)  # [3, 2, 1]

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

##################################################################
# Dicionário
##################################################################

d = {"key1": 1, "key2": "value2", "key3": [1, 2]}   # Dicionário

dict.clear( # dic.clear(
dict.get( # dic.get(
dict.mro(
dict.setdefault( # dic.setdefault(
dict.copy(  # dic.copy(
dict.items( # dic.items(
dict.pop( # dic.pop(
dict.update( # dic.update(
dict.fromkeys(  # dic.fromkeys(
dict.keys(  # dic.keys(
dict.popitem(   # dic.popitem(
dict.values(    # dic.values(

# Edições de um dicionário

d[key1]

##################################################################################
# new
##################################################################################