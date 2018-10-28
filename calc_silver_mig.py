# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 11:38:30 2017

@author: Carda Zdenek
"""
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
# =============================================================================
# calculation of Voltage from R_mig resistance
# =============================================================================
u0 = 16.5
r_mig = np.arange(0,10000000,1000, dtype=np.dtype(np.float64))
r1, r3, r4, r5 = 100000,100000,100000,100000


rc1 = r1 * r_mig / (r1 + r_mig)
rc2 = (r3 * (r4 + r5))/(r3 + r4 + r5)

u1 = u0 * rc2 / (rc1 + rc2)
u2 = u1/2

plt.plot( r_mig,u2 ,"r")


# =============================================================================
# backward calculation of R_mig resistance from Voltage
# =============================================================================

aa = r1 * u0 * rc2 - 2 * r1 * u2 * rc2 

bb = 2 * u2 * r1 -  u0 * rc2 +  u2 * 2 * rc2

#bb[ bb < 0 ] = np.minimum()

r_mig2 = aa/bb

#plt.plot(r_mig2, u2,"bx")
#


#def calculate_migration_resistance( u2  ):
#    u0  = 16
#    r1, r3, r4, r5 = 100000,100000,100000,100000
#    
#    rc2 = (r3 * (r4 + r5))/(r3 + r4 + r5)
#    
#    aa = r1 * u0 * rc2 - 2 * r1 * u2 * rc2 
#
#    bb = 2 * u2 * r1 -  u0 * rc2 +  u2 * 2 * rc2    
#    
#    r_mig = aa/bb
#    return r_mig
#
