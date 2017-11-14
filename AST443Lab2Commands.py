#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 17:44:49 2017

@author: crystalyoung (with Chris and Hu)
"""

airmass = 1/cos(90-altitude)
# 08:51:09 pm - Oxygen Deneb Image 80deg14min46sec = 80.24611°
# 12:12:31 am - Sulfur Deneb Image 45deg23min53sec = 45.39806°
# airmass found in app Stellarium using the image times
# airmass oxygen = 1.01466 ~ 1.015
# airmass sulfur = 1.40449 ~ 1.404

#Commands for Lab 2 Data Reduction

noao; twodspec; onedspecl longslit; apextract
iraf.apextract.dispaxis=1
for file in in */FIT; do mv “${file} “${file/.FIT/.fits}”; done
pyraf

#For oxygen
imcombine *flat_field* masterflat.fits combine=median
!ds9 masterflat.fits
implot masterflat.fits
c
response masterflat.fits masterflat.fits[*,38:92] flat_o.fits
yes
1
:order 20
f
imarith o_neb1.fits[*,38:92] / flat_o.fits[*,38:92] o_neb1.cf.fits
!ds9 o_neb1.cf.fits
imarith o_neb2.fits[*,38:92] / flat_o.fits[*,38:92] o_neb2.cf.fits
imarith o_neb3.fits[*,38:92] / flat_o.fits[*,38:92] o_neb3.cf.fits
imarith o_neb4.fits[*,38:92] / flat_o.fits[*,38:92] o_neb4.cf.fits
imarith o_neb5.fits[*,38:92] / flat_o.fits[*,38:92] o_neb5.cf.fits
imarith deneb_spectrum.00000007.fits[*,38:92] flat_o.fits[*,38:92] o_deneb.cf.fits
!ds9 o_deneb.cf.fits
apall o_neb1.cf.fits line=406 background=median
apall o_neb2.cf.fits line=30 background=median
apall o_neb3.cf.fits line=594 background=median
apall o_neb4.cf.fits line=594 background=median
apall o_neb5.cf.fits line=594 background=median
apall o_deneb.cf.fits line=382 background=median
scombine o_neb*.cf.ms.fits o_nebula.fits combine="average"
!splot o_nebula.fits
identify o_nebula.fits
hedit o_nebula.fits REFSPEC1 "o_nebula.fits" add=yes
hedit o_deneb.fits REFSPEC1 "o_nebula.fits" add=yes
dispcor o_nebula.fits o_nebula_L.fits
dispcor o_deneb.fits o_deneb_L.fits
epar observatory
standard o_deneb_L.fits stdspec_o caldir=onedstds$blackbody/ observatory=SBU airmass=1.015 star_name=V
obspars
SBU
1.25
V
8525
no
sensfunc stdspec_o sfunc_o
:order 18
calibrate o_nebula_L.fits o_nebula.cal.fits sensitivity="sfunc_o" extinct=no
splot o_nebula.cal.fits
wspectext o_nebula.cal.fits o_nebula.cal.txt header=no

#Measurements for 4363:
#5.77e-12, 5.77e-12, 5.95e-12 - average: 5.83e-12 -- error is 6.00e-14

## error estimated by:
#\begin{equation} \label{eq:mean}
#mean = \frac{\Sigma_i{x_i}}{N}
#\end{equation}
#
#\begin{equation} \label{eq:sigma_mean}
#\sigma_{mean} = \frac{\sqrt{\sum_i{{(x_{i}-\bar{x})}}}}{{N}}
#\end{equation}

#Measurements for 4959:
#2.03e-10. 2.06e-10, 2.03e-10 - average: 2.04e-10 -- error is 1.00e-12

#Measurements for 5007:
#7.36e-10, 7.36e-10, 7.43e-10 - average: 7.38e-10 -- error is 2.35e-12

SOLUTION: TEMPERATURE: 10885.3 Kelvin +31.5/-31.1
ratio of the fluxes (f4959 + f5007)/f4363 = 161.58 +/- 1.40


#For sulfur:
imcombine *flatfield* masterflats.fits combine=median
!ds9 masterflats.fits
implot masterflats.fits
c
response masterflats.fits masterflats.fits[*,38:90] flat_s.fits
yes
1
:order 20
f
imarith s_neb1.fits[*,38:90] / flat_s.fits[*,38:90] s_neb1.cf.fits
!ds9 s_neb1.cf.fits
imarith s_neb2.fits[*,38:90] / flat_s.fits[*,38:90] s_neb2.cf.fits
imarith s_neb3.fits[*,38:90] / flat_s.fits[*,38:90] s_neb3.cf.fits
imarith s_neb4.fits[*,38:90] / flat_s.fits[*,38:90] s_neb4.cf.fits
imarith s_neb5.fits[*,38:90] / flat_s.fits[*,38:90] s_neb5.cf.fits
imarith deneb_spectrum_s.00000033.fits[*,38:90] / flat_s.fits[38:90] s_deneb.cf.fits
!ds9 s_deneb.cf.fits
imarith neon_s_spectrum.00000026.fits[*,38:90] / flat_s.fits[*,38:90] s_neon.cf.fits
!ds9 s_neon.cf.fits
!ds9 s_neb1.cf.fits #choose line 428 for apall
apall s_neb1.cf.fits line=428 background=median
yes
1
yes
l
u
b
w
a
z
s
s
q
q
no
yes
yes
yes
yes
!ds9 s_neb2.cf.fits
#line 374
apall s_neb2.cf.fits line=374 background=median 
apall s_neb3.cf.fits line=54 background=median #same output as above
apall s_neb4.cf.fits line=128 background=median #same output as above
apall s_neb5.cf.fits line=413 background=median #same output as above
apall s_neon.cf.fits line=730 background=none 
apall s_deneb.cf.fits line=382 background=median
identify s_neon.cf.ms.fits
m
q
scombine s_neb*.cf.ms.fits s_nebula.fits combine="average"
!splot s_nebula.fits
hedit o_nebula.fits REFSPEC1 "s_neon.cf.ms.fits" add=yes
dispcor s_nebula.fits s_nebula_L.fits
hedit s_deneb.cf.ms.fits REFSPEC1 "s_neon.cf.ms.fits" add=yes
dispcor s_deneb.cf.ms.fits s_deneb_L.fits
scp v.dat
epar observatory
standard s_deneb_L.fits stdspec_s caldir=onedstds$blackbody/ observatory=SBU airmass=1.404 star_name=V bandwidth=20
obspars
SBU
magnitude of star 1.25
v band
t effective 8525
edit bandpasses=no
sensfunc stdspec_s sfunc_s
:order 23
calibrate s_nebula_L.fits s_nebula.cal.fits sensitivity="sfunc_s" extinct=no
splot s_nebula.cal.fits
wspectext o_nebula.cal.fits o_nebula.cal.txt header=no

#Measurements for 6716:
#2.45e-12, 2.53e-12, 2.53e-12 -- average: 2.50e-12
    # error: 
    
## error estimated by:
#\begin{equation} \label{eq:mean}
#mean = \frac{\Sigma_i{x_i}}{N}
#\end{equation}
#
#\begin{equation} \label{eq:sigma_mean}
#\sigma_{mean} = \frac{\sqrt{\sum_i{{(x_{i}-\bar{x})}}}}{{N}}
#\end{equation}

#Measurements for 6731:
#6.09e-12, 6.10e-12, 6.07e-12 -- average: 6.08667e-12
    # error: 0.01667e-12

ratio = 0.411 +/- 0.004 -- electron density is 10^4 or higher (agrees with paper)