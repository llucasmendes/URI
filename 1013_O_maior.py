# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
def maior(a,b):
    return (a+b+abs(a-b))/2

valores = input().split()

A = int(valores[0])
B = int(valores[1])
C = int(valores[2])

a = maior(A,B)
mai = maior(a, C)

print("%d eh o maior"%(mai,))
