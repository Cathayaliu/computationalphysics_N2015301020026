# Report 4: Throwing A Baseball
![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/4th%20homework/bangqiu.png)
***
## 摘要
在学习过计算物理的2.4节后，我决定尝试这做这样一件事情：模拟一个任意初始速度的球，并查看它在Y和Z两个方向上的轨迹。在这个模拟中，我希望引入尽可能多的自定义参数，以便于对比各种参数对轨迹的不同影响。现在的可变参数有：初始速度，发射角度，空气阻力相关参数，球的自旋速度，以及模拟的时间长度。在接下来的完善中，我将为这个模拟添加气压随高度变化带来的影响，以及球的速度变化对空气阻力造成的影响。

## 问题分析
我们将分四个部分讨论这个问题。
* 讨论描述球运动的微分方程
* 根据微分方程，使用Euler法得出近似模拟公式
* 给出相关算法和算法的Python实现
* 展示运行结果，并做一些讨论

## 球的运动微分方程
根据之前的模拟，我们可以直接得到下真空中球的运动方程：

* ![](http://latex.codecogs.com/gif.latex?\frac{dx}{dt}=v_x)

* ![](http://latex.codecogs.com/gif.latex?\frac{dy}{dt}=v_y)

* ![](http://latex.codecogs.com/gif.latex?\frac{dv_x}{dt}=0)

* ![](http://latex.codecogs.com/gif.latex?\frac{dv_y}{dt}=-g)

但是考虑到空气阻力和球的自旋，我们必须对方程做出如下修正，并增加Z方向上的速度分量和位移分量，这样才能完整地描述球的运动状态。

修正后我们得到了如下方程：

* ![](http://latex.codecogs.com/gif.latex?\frac{dx}{dt}=v_x)

* ![](http://latex.codecogs.com/gif.latex?\frac{dy}{dt}=v_y)

* ![](http://latex.codecogs.com/gif.latex?\frac{dz}{dt}=v_z)

* ![](http://latex.codecogs.com/gif.latex?\frac{dv_x}{dt}=-\frac{B_2}{m}vv_x)

* ![](http://latex.codecogs.com/gif.latex?\frac{dv_y}{dt}=-g)

* ![](http://latex.codecogs.com/gif.latex?\frac{dv_z}{dt}=-\frac{S_{0}v_{x}\omega}{m})

## 基于Euler法的数值解
我们设定时间步长Δt=0.01s,重力加速度g=9.8m/s

由Eluer法的相关知识，立刻得到：

## 算法及其Python实现
因为我引入了相当多的自定义参数，如果逐一去改变这些参数并绘图，将会使代码变得非常冗杂，修改相关变量会成为一个噩梦。因此本程序将使用所谓“枪弹分离”的设计。我将自定义一个以所有自定义参数为变量的函数，并在另一个文件里调用这个函数输出图像。这样我们便实现了效率和效果的平衡。

首先我们来看一下这个函数的设计：
```
import matplotlib.pyplot as plt
import math

def A_FLY_BALL(V0,A,W,S0,B2,LIM):
    
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
```

