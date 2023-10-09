#!/usr/bin/env python
# coding: utf-8

# # Уровень 0
# 
# Представим фильмы в виде бинарных векторов (numpy array) используя следующие признаки:
# 
# [Комедия, Боевик, Исторический, Бред Питт, Бенедикт Камбербэтч, Квентин Тарантино]
# 
# Игра в имитацию
# 
# Ярость
# 
# 12 лет рабства
# 
# Однажды в Голливуде

# In[7]:


import pandas as pd
import numpy as  np
import sympy as sym
import matplotlib.pyplot as plt


# In[5]:


film_1 = np.array([0,0,0,0,1,0])      # Игра в имитацию

film_2 = np.array([0,1,0,1,0,0])      # Ярость

film_3 = np.array([0,0,1,1,1,0])      # 12 лет рабства

film_4 = np.array([1,0,0,1,0,1])      # Однажды в Голливуде


# ## Задание 1
# Найти угол между векторами-фильмами "Ярость" и "12 лет рабства". Результатом будет являться косинусная мера, которую можно использовать для определения похожести векторов.

# In[23]:


# plt.figure()
# plt.plot(film_1[0], film_1[1], film_1[2], film_1[3], film_1[4], film_1[5], 'b+')
# plt.plot(film_2[0],film_2[1],film_2[2],film_2[3],film_2[4],film_2[5], 'r*')
# plt.plot(film_3[0],film_3[1],film_3[2],film_3[3],film_3[4],film_3[5], 'go')
# plt.plot(film_4[0],film_4[1],film_4[2],film_4[3],film_4[4],film_4[5], 'brown')
# plt.grid()
# plt.xlim([-6,6])
# plt.ylim([-6,6])
# plt.show()


# In[39]:


print(f'Норма вектора фильма "Ярость" = {np.linalg.norm(film_2)}')
print(f'Норма вектора фильма "12 лет рабства" = {np.linalg.norm(film_3)}')


# In[49]:


print(f'Косинусная мера угла между вектороами фильмов "Ярость" и  "12 лет рабства" = {np.dot(film_2,film_3) /( np.linalg.norm(film_2) * np.linalg.norm(film_3))}')


# In[72]:


print (f' градусов между векторами {np.rad2deg(np.arccos(np.dot(film_2,film_3) /( np.linalg.norm(film_2) * np.linalg.norm(film_3))))}')


# # Уровень 1
# 
# ## Задание 1
# 
# Вычислить с помощью Python значение первой производной для функции 8x(x + 3)**2 в точке x = 1

# In[74]:


x = sym.Symbol('x')


# In[79]:


8*x*(x + 3)**2


# In[82]:


res = sym.diff(8*x*(x + 3)**2)
res


# In[84]:


res.subs(x,1)


# ## Задание 2
# Объединить векторы фильмов в матрицу, где каждый вектор является строкой матрицы. Умножьте вектор [1,2,3,4] на полученную матрицу

# In[100]:


# mat = [list(film_1), list(film_2), list(film_3), list(film_4)]
#mat

mat = [film_1, film_2, film_3, film_4]
mat


# In[104]:


vec = np.array([1,2,3,4])


# In[109]:


result = np.dot(vec,mat)
result

