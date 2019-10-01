# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 18:22:22 2019

@author: lluca
"""

N = int(input())

if 0 < N < 1000000:    
    cem = N // 100
    cemx = N % 100
    cinq = cemx // 50
    cinqx = cemx % 50
    vint = cinqx // 20
    vintx = cinqx % 20
    dez = vintx // 10
    dezx = vintx % 10
    cinc = dezx // 5
    cincx = dezx % 5
    dois = cincx // 2
    doisx = cincx % 2
    um = doisx
print (N)
print("%d nota(s) de R$ 100,00" % cem)
print("%d nota(s) de R$ 50,00" % cinq)
print("%d nota(s) de R$ 20,00" % vint)
print("%d nota(s) de R$ 10,00" % dez)
print("%d nota(s) de R$ 5,00" % cinc)
print("%d nota(s) de R$ 2,00" % dois)
print("%d nota(s) de R$ 1,00" % um)
