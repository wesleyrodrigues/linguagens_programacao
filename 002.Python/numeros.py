# 5
# 3, 6, 9

from random import choice, randint
from pyperclip import copy

dic = {}

for i in range(1, 27):
    dic.update({i: chr(64 + i)})

for i in range(65, 91):
    dic.update({i: chr(i)})

for i in range(97, 123):
    dic.update({i: chr(i).upper()})

def rand_fun_all(num):
    return f"""{num}
        {rand_fun(num)}
        {rand_fun(num + 3)}
        {rand_fun(num + 6)}
        {rand_fun(num + 9)}
        {rand_fun(num - 3)}
        {rand_fun(num - 6)}
        {rand_fun(num - 9)}
        {rand_fun(num * 3)}
        {rand_fun(num * 6)}
        {rand_fun(num * 9)}
        {rand_fun(num // 3)}
        {rand_fun(num // 6)}
        {rand_fun(num // 9)}
        """


def rand_fun(num):
    num = abs(num)
    try:
        strcopyone = dic[num]
        return strcopyone
    except(KeyError):
        if(num == 0):
            return "Zero"
        
        num = list(str(num))
        num = sum(list(map(int, num)))
        strcopyone = dic[num]
        return strcopyone

while(True):
    a = int(input("Number: "))
    if(a == 0):
        break
    rand_num = randint(1, 122)
    print(a)
    print(rand_num)
    str_copy = rand_fun_all(a)
    str_copy += rand_fun_all(rand_num)
    copy(str_copy)
        # copy(dic[b_int])