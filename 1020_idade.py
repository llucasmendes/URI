# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 17:13:16 2019

@author: lluca
"""

dias = int(input())

anos = dias // 365
meses = (dias % 365) // 30
dia = ((dias % 365) % 30)

print("%d ano(s)" % anos)
print("%d mes(es)" % meses)
print("%d dia(s)" % dia)