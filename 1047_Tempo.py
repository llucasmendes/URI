# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 16:14:09 2019

@author: lluca
"""

valores = input().split()

h1 = int(valores[0])
m1 = int(valores[1])
h2 = int(valores[2])
m2 = int(valores[3])

inicio = h1*60 + m1
final = h2*60 + m2
duracao = 0
horas = 0
minutos = 0

if h1 <= h2:
    duracao = final - inicio
    if duracao == 0:
        horas = 24
        minutos = duracao%60
    else:
        horas = (duracao - duracao%60)/60
        minutos = duracao%60
else:
    duracao = (24*60 - inicio) + final
    horas = (duracao - duracao%60)/60
    minutos = duracao%60
    
print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)"%(horas, minutos))