# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 18:09:11 2019

@author: lluca
"""

consumo = 12

horas = int(input())
velocidade = int(input())

con = (velocidade*horas)/consumo

print("%.3f" % con)