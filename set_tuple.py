# "=========Кортежы=========="
# # Кортежы - неизменяемый, индексируемый, упорядоченный, итерируемый тип данных, предназначены для хронения любых даднных в определеном порядке

# tuple1 = (1,2,3,4, 'hello', [1,2], {'a' : 'b'}, false, None)
# tuple1[0] # 1
# tuple1[4][2] # l

# "======Методы кортежей======="

# print(dir(tuple))
#  # count -  считает количество принятого элемента
# tuple1 - (1,2,3,4,5,1,2.3)
# print(tuple1.count(1)) # 2
# print(tuple1.count(3)) # 2

# # index - возвращяет индекс первого попавшгося элемента
# tuple = (,2,3,4,5,1,2.3)
# tuple1.index(5) # 4

# "=======Множества========="
# # Множества - изменяемый , неупорядоченный, неиндексируемый, итерируемый тип данных, предназначены для хранения уникальных (множерство может хронить только не изменяемый типы данных)

# set_ = {1,2,3,4,5} #{,}
# a = {}
# print(type(a)) # dict

# set_ = set() # {} - Множества
# set_ - {'hello', 1,2, 'hello'} #{'hello', 1,2} or {1,2, 'hello'}...........................
# # print(set_[0])
# for i in set :
#     print(i)

# print('hello'in set_) # True
# print('hell'in set_) # False

# list_ = [1.2.3.4.5.6.1.12,21,1,1,12]
# list_ = list(set(list_)) # [1,2,3,4,5,6,12,21]

# "==============Методы множеств===================="
# # add - добавляет элемент в set

# set_ = {1,2,3}
# set_ .add(4)
# set_.add('a')
# # print(set_) # {1,2,3,4, 'a'}

# pop - удаляет элемент по принципу FIFO 
# set_ = {'aasdf',1,2,3,4}
# popped = set_.pop()
# print(set_, popped) # {'aasdf',2,3,4}

# remeove
set_ = {'aasdf',1,2,3,4}
set_.remove('aasdf')
print(set_)

# inersection - находит пересечения между set и другими колекциями (&)

set1 = {1,2,3,4}
set2 = {3,4,5,6}
print(set1.intersection(set2)) # {3.4}
print(set1 & set2) #  {3,4}

if
set1 = {1,2,3,4}
set2 = {3,4,5,6}
set2 = list(set2)
print(set1.intersection(set2)) # {3.4}
print(set1 & set2) #  Error

# differentce - находит отличия относительно первого set (-)

set1 = {1,2,3,4}
set2 = {3,4,5,6}
print(set1.difference(set2)) # {1,2}
print(set1.difference(set1)) # {5,6}
print(set1 & set2) #  {3,4}

if 
set1 = {1,2,3,4}
set2 = {3,4,5,6}
print(set1.difference(set2)) # {1,2}
print(set1 - set2) #  Error

# symmetric_difference

set1 = {1,2,3,4}
set2 = {3,4,5,6}
print(set1.symmetric_difference(set2)) # {1,2,5,6}


# symmetric_difference_update -  обновит set1

set1 = {1,2,3,4}
set2 = {3,4,5,6}
print(set1.symmetric_difference_update(set2)) # {1,2,5,6}
print(set1) # {1,2,5,6}

# discard - удаляет элеент по значению если нет такого элемента не выдает оштбку

set1 = {1,2,3,4}
set1.discard(5)
print(set1)

# union, issubset - HOME WORK


tuple = 