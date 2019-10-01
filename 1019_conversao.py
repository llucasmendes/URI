# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 19:50:18 2019

@author: lluca
"""

tempo = int(input())

horas = tempo // 3600
minutos = (tempo % 3600) // 60
segundos = ((tempo % 3600) % 60) 

print("%d:%d:%d" % (horas, minutos, segundos))