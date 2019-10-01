# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 17:35:45 2019

@author: lluca
"""
import math

def distancia(x1,x2,y1,y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

valores = input().split()

x1 = float(valores[0])
y1 = float(valores[1])

valor = input().split()

x2 = float(valor[0])
y2 = float(valor[1])

dist = distancia(x1,x2,y1,y2)

print("%.4f"%(dist,))