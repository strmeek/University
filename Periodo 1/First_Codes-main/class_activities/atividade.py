# -*- coding: utf-8 -*-
"""Atividade.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GQ5IOFF3hQTUrxxIk9_A8iDOz0EXAnKg
"""

#lista aleatória
import random as rd

lista = []

for i in range(20):
  a = rd.randint(1,5000)
  lista.append(a)

#Separar em pares e impares
par = []
impar = []

for enumerate in lista:
  if enumerate % 2 == 0:
    par.append(enumerate)
  else:
    impar.append(enumerate)

print("20 números aleatórios: %s" %(lista))
print("lista de pares: %s" %(par))
print("lista de impares: %s" %(impar))

#Temperaturas mensais

import random as rd

temp = []

for i in range(12):
  t = rd.randint(5,40)
  temp.append(t)

#média das temperaturas

x = sum(temp) / 12

print("Temperatura Média Anual: %d" %x)

#Resultados Acima da Média

total = { temp[0] : "Janeiro",
         temp[1] : "Fevereiro",
         temp[2] : "Março",
         temp[3] : "Abril",
         temp[4] : "Maio",
         temp[5] : "Junho",
         temp[6] : "Julho",
         temp[7] : "Agosto",
         temp[8] : "Setembro",
         temp[9] : "Outubro",
         temp[10] : "Novembro",
         temp[11] : "Dezembro" }

print("Meses Acima da Média: ")

for enumerate in temp:
  months = []
  if enumerate > x:
    k = temp.index(enumerate)
    print(total[temp[k]],"-",temp[k])