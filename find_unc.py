#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 15:14:13 2017

@author: crystalyoung
"""

# This is a program to find the uncertainty measurements in the ratio of the fluxes for oxygen and for sulfur

import math

#5.77e-12, 5.77e-12, 5.95e-12 , average is 5.83e-12
s = math.sqrt((5.77e-12 - 5.83e-12)**2 + (5.77e-12 - 5.83e-12)**2 + (5.95e-12 - 5.83e-12)**2) / 3#(math.sqrt(2) * math.sqrt(3))
print(s) # error in 4363 # 4.90e-14

#2.03e-10. 2.06e-10, 2.03e-10 , average is 2.04e-10
q = math.sqrt((2.03e-10 - 2.04e-10)**2 + (2.06e-10 - 2.04e-10)**2 + (2.03e-10 - 2.04e-10)**2) / 3#(math.sqrt(2) * math.sqrt(3))
print(q) # error in 4959 # 8.16e-13

#7.36e-10, 7.36e-10, 7.43e-10 , average is 7.38e-10 
w = math.sqrt((7.36e-10 - 7.38e-10)**2 + (7.36e-10 - 7.38e-10)**2 + (7.43e-10 - 7.38e-10)**2) / 3#(math.sqrt(2) * math.sqrt(3))
print(w) # error in 5007 # 1.91e-12

#Measurements for 6716:
#2.45e-12, 2.53e-12, 2.53e-12 -- average: 2.50e-12
y = math.sqrt((2.45e-12 - 2.50e-12)**2 + (2.53e-12 - 2.50e-12)**2 + (2.53e-12 - 2.50e-12)**2) / 3#(math.sqrt(2) * math.sqrt(3))
print(y) #error in 6716 # 2.19e-14

#Measurements for 6731:
#6.09e-12, 6.10e-12, 6.07e-12 -- average: 6.08667e-12
u = math.sqrt((6.09e-12 - 6.09e-12)**2 + (6.10e-12 - 6.09e-12)**2 + (6.07e-12 - 6.09e-12)**2) / 3#(math.sqrt(2) * math.sqrt(3))
print(u) # error in 6731 # 7.44e-15

# For sulfur
f6716 = 2.50e-12
f6731 = 6.08667e-12
result = f6716 / f6731

err6716 = 2.19e-14 # 0.05e-12
err6731 = 7.44e-15 # 0.06e-12

#print(result)

s = math.sqrt(((err6716/f6731)**2 + (f6716/f6731**2)**2*(err6731**2)))
print("%.3f" % result, "+/-", "%.3f" % s)

#si = result * math.sqrt((err6716/f6731)**2+(err6731/f6731)**2)
#print(si)

# For oxygen
f4959 = 2.04e-10
f5007 = 7.38e-10
fcom = f4959 + f5007
f4363 = 5.83e-12
result = fcom / f4363

err4363 = 4.90e-14 #0.12e-12
err4959 = 8.16e-13 #0.02e-10
err5007 = 1.91e-12 #0.05e-10
errcom = err4959 + err5007

#------

T = 10885.3
#sigma_T = math.sqrt(((err5007/f4363)**2 + (err4959/f4363)**2 + (((f5007 + f4959)*err4363)/f4363)**2) / ((1.7775*math.e**(32600/T)*(T-146222*math.sqrt(T)-65800))/((math.sqrt(T)+0.45)**2*T**(3/2)))**2)
#print(sigma_T)

#print(result)

sig =  math.sqrt(((err5007/f4363)**2 + (err4959/f4363)**2 + ((f5007 + f4959)/f4363**2)**2*(err4363**2)))
print("%.3f" % result, "+/-", "%.3f" % sig)

#sig2 = result * math.sqrt((errcom/fcom)**2+(err4363/f4363)**2)
#print(sig2)

