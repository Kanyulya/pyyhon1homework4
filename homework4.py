# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# d = float(input('введите значение точности d: '))
# p = 3.141592653589
# count  = 0
# while d%1!=0:
#     d=d*10
#     count+=1
# # print(count)
# print(round(p*1,count))

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# n=int(input('Введите число: '))
# spisok=[]
# delit = 1
# i=1
# while i in range(1,100000):           # пока не знаю как писать бесконечность
#     if n%delit==0:
#         spisok.append(i)
#         n=n/delit
#         delit+=1
#         i+=1
    
#     else:
#         delit+=1
#         i+=1

# print(spisok)

# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# nums = [2,3,7,1,6,3,27,1,11,33,5,2,4,3,2,5,6,5,3,2]
# li =[]
# for i in range(len(nums)):       
#     s=nums.count(nums[i])
#     if s ==1:
#         # print(nums[i])
#         li.append(nums[i])
# print(li)


# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# k = int(input('введите число: '))

# arr = []
# import random
# for i in range(0, k+1):
#     arr.append(random.randint(1, 100))              
#     if i+1<k:
#         print(arr[i], '*x^', k-i, '+', end=' ')
#     elif i+1==k: print(arr[i], '*x', '+', end=' ') 
#     else: print(arr[k], '= 0')
# print(arr)


# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

# не справилась, посмотрю решение в записи семинара
# понимаю, что нужно считать коэффициенты, дальше работать с ними
# при этом должны быть добавлены условия при отсутствии х в первой степени, или при отсутствии свободного элемента многочлена
