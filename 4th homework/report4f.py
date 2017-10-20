# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 15:53:27 2017

@author: Administrator
"""

import matplotlib.pyplot as plt
import math

def A_FUCK_BALL(V0,A,W,S0,B2,LIM):
    
    X=[0 for x in range(0,LIM)]
    Y=[0 for x in range(0,LIM)]
    Z=[0 for x in range(0,LIM)]

    X[0]=0
    Y[0]=0
    Z[0]=0

    T=0.01
    g=9.8

    VX=V0*math.cos(A)
    VY=V0*math.sin(A)
    VZ=0
    V=V0
    for i in range(1,LIM):
        VX=VX-(B2*V*VX)*T
        VY=VY-g*T
        VZ=VZ-(S0*W*VX)*T
        V=(VX*VX+VY*VY+VZ*VZ)**0.5
        X[i]=X[i-1]+VX*T
        Y[i]=Y[i-1]+VY*T
        Z[i]=Z[i-1]+VZ*T
    
    P1=plt.plot(X,Y)
    P2=plt.plot(X,Z)
    
    return P1,P2




