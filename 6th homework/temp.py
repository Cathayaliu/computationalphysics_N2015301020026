import math
from matplotlib import pyplot as plt

def Chaos(OMGD,Ts,L,Q):
    
    g=9.8
    T=0.01
    LIM=int(Ts/T)
        
    ω=[0 for x in range(0,LIM)]
    θ=[0 for x in range(0,LIM)]
    t=[0 for x in range(0,LIM)]
    D=[]
    F=[]
    FD=1.2
    ω[0]=0
    θ[0]=0.2
    t[0]=0
    
        
    for i in range(0,LIM-1):
        ω[i+1]=ω[i]-((g/L)*math.sin(θ[i])+Q*ω[i]-FD*math.sin(OMGD*t[i]))*T
        θ[i+1]=θ[i]+ω[i+1]*T
        if θ[i+1]<-math.pi:
            θ[i+1]=θ[i+1]+2*math.pi
        elif θ[i+1]>math.pi:
            θ[i+1]=θ[i+1]-2*math.pi
        else:
            θ[i+1]=θ[i+1]    
        t[i+1]=t[i]+T
        if ((OMGD*t[i+1])/(2*math.pi)-int((OMGD*t[i+1])/(2*math.pi))<(OMGD*T)/(2*math.pi)):
                D.append(θ[i+1])
                F.append(ω[i+1])
        
        
    return [F,D]

plt.scatter(Chaos(2/3,5000,9.8,0.5)[1],Chaos(2/3,5000,9.8,0.5)[0],s=1)
plt.xlabel(r'$\theta (radians)$')
plt.ylabel(r'$\omega (radians/s)$')
plt.title(r'$\omega\ versus\ \theta$')


