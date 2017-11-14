#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 17:24:37 2017

@author: chris
"""

#############################################################################
# Code to import a text file and plot it. Text file is tab seperated.
# Markers are added for emission lines in each plot with plt.annotate.
# Two text files are loaded, comment out whichever half of the code that
# is not needed.
#############################################################################

### Use numpy to load text
import numpy as np
### For plotting
import matplotlib.pyplot as plt

#############################################################################
# Comment out the second half of the code for a plot of s_nebula2.txt only.
#############################################################################

### Load text file for sulfur measurements
text_file = np.loadtxt('s_nebula2.txt')
### x axis is the first column, y axis is the second
x = text_file[:,0]
y = text_file[:,1]

### Plot y vs x
plt.plot(x,y)

### Put in markers for each observable emission line
plt.annotate('6716.4', xy=(6716, 2.5e-12), xytext=(6695, 0.4e-10),
            arrowprops=dict(arrowstyle='->'))
plt.annotate('[S II]', xy=(6716, 2.5e-12), xytext=(6700, 0.45e-10))

plt.annotate('6731.8', xy=(6731, 2.5e-12), xytext=(6780, 0.8e-10),
            arrowprops=dict(arrowstyle='->'))
plt.annotate('[S II]', xy=(6731, 2.5e-12), xytext=(6790, 0.85e-10))

plt.annotate('6363.8', xy=(6363.8, 2.5e-12), xytext=(6345, 0.5e-10),
            arrowprops=dict(arrowstyle='->'))
plt.annotate('[O I]', xy=(6763, 2.5e-12), xytext=(6350, 0.55e-10))

plt.annotate('6435.1', xy=(6435, 1.5e-12), xytext=(6415, 0.3e-10),
            arrowprops=dict(arrowstyle='->'))
plt.annotate('[Ar V]', xy=(6735, 2.5e-12), xytext=(6420, 0.35e-10))

plt.annotate('6548.1', xy=(6548, 0.16e-10), xytext=(6495, 0.7e-10),
            arrowprops=dict(arrowstyle='->'))
plt.annotate('[N II]', xy=(6548, 2.5e-12), xytext=(6500, 0.75e-10))

plt.annotate('6562.9', xy=(6562, 1.25e-10), xytext=(6545, 1.4e-10),
            arrowprops=dict(arrowstyle='->'))
plt.annotate('H 3', xy=(6562, 1.25e-10), xytext=(6560, 1.45e-10))

plt.annotate('6583.5', xy=(6583, 0.45e-10), xytext=(6595, 1.0e-10),
            arrowprops=dict(arrowstyle='->'))
plt.annotate('[N II]', xy=(6583, 0.5e-10), xytext=(6600, 1.05e-10))

plt.annotate('6678.2', xy=(6678, 2.5e-12), xytext=(6645, 0.7e-10),
            arrowprops=dict(arrowstyle='->'))
plt.annotate('He I', xy=(6678, 2.5e-12), xytext=(6650, 0.75e-10))

plt.annotate('7006.0', xy=(7005, 2.5e-12), xytext=(6985, 0.5e-10),
            arrowprops=dict(arrowstyle='->'))
plt.annotate('[Ar V]', xy=(7005, 2.5e-12), xytext=(6990, 0.55e-10))

### Sey y limit, title and axis labels
plt.ylim(ymax=1.6e-10)
plt.title('NGC 7027 Emisson Spectrum ($6312\AA - 7067\AA$)') 
plt.xlabel('Wavelength ($\AA$)')
plt.ylabel('Flux ($erg/s/cm^2/Hz$)')
plt.show()

############################################################################
# Comment everything above this to only show one plot at a time
############################################################################

### Load text file for oxygen measurements
text_file = np.loadtxt('o_nebula3.txt')
### Set x and y
x2 = text_file[:,0]
y2 = text_file[:,1]

### Plot y vs x
plt.plot(x2,y2)
### Put in markers for each observable emission line
plt.annotate('4340.5', xy=(4340.5, 2.5e-12), xytext=(4320, 0.4e-10),
            arrowprops=dict(arrowstyle='->'))
plt.annotate('H 5', xy=(4340.5, 2.5e-12), xytext=(4330, 0.5e-10))

plt.annotate('4363.2', xy=(4363.2, 2.5e-12), xytext=(4350, 0.6e-10),
            arrowprops=dict(arrowstyle='->'))
plt.annotate('[O III]', xy=(4363.2, 2.5e-12), xytext=(4360, 0.7e-10))

plt.annotate('4685.9', xy=(4685.9, 0.05e-10), xytext=(4670, 0.6e-10),
            arrowprops=dict(arrowstyle='->'))
plt.annotate('He II', xy=(4685.9, 0.05e-10), xytext=(4675, 0.7e-10))

plt.annotate('4861.5', xy=(4861.5, 0.2e-10), xytext=(4845, 0.7e-10),
            arrowprops=dict(arrowstyle='->'))
plt.annotate('H 4', xy=(4861.5, 0.2e-10), xytext=(4850, 0.8e-10))

plt.annotate('4959.0', xy=(4959, 0.75e-10), xytext=(4945, 1.4e-10),
            arrowprops=dict(arrowstyle='->'))
plt.annotate('[O III]', xy=(4949, 0.75e-10), xytext=(4950, 1.5e-10))

plt.annotate('5006.9', xy=(5006.9, 2.25e-10), xytext=(4990, 2.7e-10),
            arrowprops=dict(arrowstyle='->'))
plt.annotate('[O III]', xy=(5006.9, 2.5e-10), xytext=(4995, 2.8e-10))

plt.annotate('4740.4', xy=(4740.4, 0.06e-10), xytext=(4725, 0.5e-10),
            arrowprops=dict(arrowstyle='->'))
plt.annotate('[Ar IV]', xy=(4740.4, 0.06e-10), xytext=(4730, 0.6e-10))

### Sey y limit, title and axis labels
plt.ylim(ymax=3.0e-10)
plt.title('NGC 7027 Emisson Spectrum ($4314\AA - 5022\AA$)') 
plt.xlabel('Wavelength ($\AA$)')
plt.ylabel('Flux ($erg/s/cm^2/Hz$)')
plt.show()
