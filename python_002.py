# работа со строками
"""
string1 = "This is a string.  "
string2 = "  This is another string."
string3 = string1 + string2
string4 = "00Some string00"
print(string3)

print(len(string1))
print(string1.title())
print(string1.lower())
print(string1.upper())
print(string1.rstrip())
print(string2.lstrip())
print(string1.strip())
print(string4.strip('0'))

#извлечение символов и подстрок

d = 'qwerty'
ch = d[2]
print(ch)
chm = d[1:3]
print(chm)
#d[2] = 'Z'
d = d.replace('q', 'Zzzz')
print(d)

#работа с числами

x = int(5)
y = int(8)
print(x/y)
print(x%2)
print(y**2)


#преобразование данных

x = int(5)
param = "string" + str(x)
print(param)

n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
n3 = float(n1) + float(n2)
#print(n1 + " plus " + n2 + " = ", n3)
print("{:7.1f} plus {:7.1f} = {:7.1f}".format(n1, n2, n3))

#форматирование строк

a = 1/3
#help(format)
print("{:7.3f}".format(a))

a = 2/3
b = 2/9
print("{:7.3f} {:7.3f}".format(a, b))
print("{:10.3e} {:10.3e}".format(a, b))


# списки

list1 = [82, 8, 23, 97, 92, 44, 17, 39, 11, 12]
print(dir(list))
list1[0] = 666
print(list1)

list1.append(999)
print(list1)

list1.insert(5, 555)
print(list1)

list1.remove(list1[0])
print(list1)

list1.pop()
print(list1)



# сортировка элементов списка

list1 = [82, 8, 23, 97, 92, 44, 17, 39, 11, 12]
list1.sort()
print(list1)
list1.reverse()
print(list1)

list2 = [3, 5, 6, 2, 33, 6, 11]
list3 = sorted(list2)
print(list3)
print(list2)


# кортежи

# print(dir(tuple))
# help(tuple.index)
# help(tuple.count)

seq = (2, 8, 23, 97, 92, 44, 17, 39, 11, 12)
print(seq.count(8))
print(seq.index(44))

print(seq)
listseq = list(seq)
print(listseq)


#словари

D = {'food': 'Apple', 'quantity': 4, 'color': 'Red'}
print(D['food'])
print(D)
D['quantity'] += 10
print(D)

dp = {}

#help(dict)

def print_tuple(a):
    print(a)

def fill_tuple(a):
    return a.update({'name': input("Enter the name: "), 'age': input("Enter the age: ")})

print_tuple(dp)
fill_tuple(dp)
print_tuple(dp)

"""

#вложенность хранения данных

rec = {'name': {'firstname': 'Bob', 'lastname': 'Smith'},
        'job': ['dev', 'mgr'],
        'age': 25}

print(rec['name']['firstname'] + " " + rec['name']['lastname'])
print(rec['name']['firstname'])
print(rec['job'])
rec['job'].append('janitor')
print(rec['job'])
print(rec)
