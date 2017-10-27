# Report: Chaos in the Driven Nonlinear Pendulum
### Author: Cathaya Liu *2015301020026*

## 前言
本周我们学习了计算物理的第三章，对于Chaos这个主题期待已久~因此想尽可能多地改变一下相关参数，看能不能得到一些有趣的结果。这次报告不会针对课后作业的某个具体问题，而是对所有问题都有涉及。比起具体的问题，我更喜欢讨论“泛用”的方法。
## 摘要
本次我打算涉及的主题有：
* 绘制θ-t, θ-ω的关系图
* 研究不同的驱动力、空气阻力因子、绳长等因素对θ的影响
* 绘制Δθ-t的关系图，展示混沌系统对初值条件的敏感性
* 绘制吸引子图，展示吸引子的稳定性
* 探索哪些因素会影响吸引子
## 原理与算法


## 算法的Python实现
* 本次代码使用了类方法，通过在类中定义一系列函数，较好地减少了代码量，提高了重用率和效率。
首先，我们引入相关包
```
from matplotlib import pyplot as plt
import math
```
然后，定义一个类，命名为Chaos，专门处理混沌的问题，在这个类下定义有三个函数，稍后我会对它们的功能逐一进行说明。之后有关混沌的函数和方法也会被加入到这个类里。
```
class Chaos:
```
接下来，我们定义第一个函数。这个函数的功能是返回一个二维列表，列表中包含有θ、ω的全部信息以及绘制吸引子图所需要的全部信息。
```    
    def Chaos_Cathaya(FD,OMGD,LIM,L,Q,xita):
        
        ω=[0 for x in range(0,LIM)]
        θ=[0 for x in range(0,LIM)]
        t=[0 for x in range(0,LIM)]
    
        ω[0]=0
        θ[0]=xita
        t[0]=0
    
        g=9.8
        T=0.04
    
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
    
        ωa=ω[0::int(math.pi*3/(T))]
        θa=θ[0::int(math.pi*3/(T))]
        
        CHAOSET=[ω,θ,ωa,θa]
        
        return CHAOSET
```
第二个函数专门用来计算Δθ,通过对第一个函数的调用，较为简洁地完成了这个任务。
```
    def Chaos_Compare(DIF,FD,OMGD,LIM,L,Q,xita):
        
        Dθ=[0 for x in range(0,LIM)]
        Dθ[0]=DIF
        
        for i in range(0,LIM):
            Dθ[i]=Chaos.Chaos_Cathaya(FD,OMGD,LIM,L,Q,xita+DIF)[1][i]-Chaos.Chaos_Cathaya(FD,OMGD,LIM,L,Q,xita)[1][i]
            
        return Dθ
```
我们画的很多图中都需要时间t作为横坐标，而仅仅是为了时间t去调用第一个函数实在是太没有效率了。因此我专门定义了下面这个函数，用来提供绘图所需的时间标度。
```
    def Timeline(LIM,T):
        
        t=[0 for x in range(0,LIM)]
        t[0]=0
        
        for i in range(0,LIM-1):
            t[i+1]=t[i]+T
            
        return t
```
