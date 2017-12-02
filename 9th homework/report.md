# Report: The Three-body Problem
### 2015301020026 Cathayaliu
***
![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/9th%20homework/9675CD87877DB394415C7116253F7162.jpg)
***
## 摘要
本次模拟的是太阳系中木星、地球和太阳的三体模型。采用了质心坐标系和总动量为0的设定。

## 程序
```
import matplotlib.pyplot as plt
import math

xita1=math.pi/3
xita2=math.pi/1
ve0=2*math.pi
vj0=0.9*math.pi

vex=[ve0*math.sin(math.pi-xita1)]
vey=[ve0*math.cos(math.pi-xita1)]
vjx=[vj0*math.sin(math.pi-xita2)]
vjy=[vj0*math.cos(math.pi-xita2)]


t=[0]
delta_T=0.001
ms=2*10**28
def giveloc(me,mj,time):
    T=int(time/delta_T)
    xe0=1*math.cos(xita1)
    ye0=1*math.sin(xita1)
    xj0=5.2*math.cos(xita2)
    yj0=5.2*math.sin(xita2)
    
    y0=(ye0*me+yj0*mj)/(me+mj)
    x0=(xe0*me+xj0*mj)/(me+mj)
    vsx0=-(me*vex[0]+mj*vjx[0])/ms
    vsy0=-(me*vey[0]+mj*vjy[0])/ms
    
    vsy=[vsy0]
    vsx=[vsx0]
    xe=[1*math.cos(xita1)-x0]
    ye=[1*math.sin(xita1)-y0]
    xj=[5.2*math.cos(xita2)-x0]
    yj=[5.2*math.sin(xita2)-y0]
    xs=[0-x0]
    ys=[0-y0]
    for i in range(0,T):
        res=math.sqrt((xe[i]-xs[i])**2+(ye[i]-ys[i])**2)
        rjs=math.sqrt((xj[i]-xs[i])**2+(yj[i]-ys[i])**2)
        rej=math.sqrt((xe[i]-xj[i])**2+(ye[i]-yj[i])**2)
            
        vexm=vex[i]-(4*math.pi**2*(xe[i]-xs[i])*delta_T)/(res**3)-(4*math.pi**2*(mj/ms)*(xj[i]-xe[i])*delta_T)/(rej**3)
        vex.append(vexm)
        veym=vey[i]-(4*math.pi**2*(ye[i]-ys[i])*delta_T)/(res**3)-(4*math.pi**2*(mj/ms)*(yj[i]-ye[i])*delta_T)/(rej**3)
        vey.append(veym)
            
        vjxm=vjx[i]-(4*math.pi**2*(xj[i]-xs[i])*delta_T)/(rjs**3)-(4*math.pi**2*(me/ms)*(xj[i]-xe[i])*delta_T)/(rej**3)
        vjx.append(vjxm)
        vjym=vjy[i]-(4*math.pi**2*(yj[i]-ys[i])*delta_T)/(rjs**3)-(4*math.pi**2*(me/ms)*(yj[i]-ye[i])*delta_T)/(rej**3)
        vjy.append(vjym)
        
        vsxm=vsx[i]-(4*math.pi**2*(me/ms)*(xs[i]-xe[i])*delta_T)/(res**3)-(4*math.pi**2*(mj/ms)*(xs[i]-xj[i])*delta_T)/(rjs**3)
        vsx.append(vsxm)
        vsym=vsy[i]-(4*math.pi**2*(me/ms)*(ys[i]-ye[i])*delta_T)/(res**3)-(4*math.pi**2*(mj/ms)*(ys[i]-yj[i])*delta_T)/(rjs**3)
        vsy.append(vsym)
            
        xeim=xe[i]+vex[i+1]*delta_T
        xe.append(xeim)
        yeim=ye[i]+vey[i+1]*delta_T
        ye.append(yeim)
        xjim=xj[i]+vjx[i+1]*delta_T
        xj.append(xjim)
        yjim=yj[i]+vjy[i+1]*delta_T
        yj.append(yjim)
        xsim=xs[i]+vsx[i+1]*delta_T
        xs.append(xsim)
        ysim=ys[i]+vsy[i+1]*delta_T
        ys.append(ysim)

    p1=plt.scatter(xe,ye,s=1)
    p2=plt.scatter(xj,yj,s=1)
    p3=plt.scatter(xs,ys,s=1)
    plt.legend([p1,p2,p3], ['Earth', 'Jupiter','Sun'])
    ax = plt.gca()
    ax.set_aspect(1)
        
    return plt.show()

```

## 结果
下图分别是木星质量从1/1000MJ到1000MJ的模拟图，时长50年，步长0.001年，初始夹角0
![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/9th%20homework/Figure_1.png)
![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/9th%20homework/Figure_1-1.png)
![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/9th%20homework/Figure_1-2.png)
![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/9th%20homework/Figure_1-3.png)
![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/9th%20homework/Figure_1-4.png)

注意到直观来看地球轨道开始越来越粗了……只画地球轨道如下图：

![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/9th%20homework/Figure_1-5.png)

继续：

![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/9th%20homework/Figure_1-7.png)
![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/9th%20homework/Figure_1-6.png)

当木星质量变为1000MJ时，有趣的事情开始了：以下分别是0，90，180度夹角的情况

![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/9th%20homework/Figure_1-8.png)
![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/9th%20homework/Figure_1-9.png)
![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/9th%20homework/Figure_1-10.png)

可以看出地球有时彻底逃逸，有时被太阳俘获。

接下来开始放飞自我，改变地球质量为100ME和1000ME，得到下图：

![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/9th%20homework/Figure_1-13.png)
![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/9th%20homework/Figure_1-14.png)


## 结论
当地球质量和木星质量远小于太阳质量时，可以稳定运动，有闭合轨道。

当木星质量和太阳质量相近时，地球可能被其中之一俘获，也可能逃逸。

当三者质量相近时，根据初始条件不同，可能会有一段时间的混沌现象，但最终逃逸可能性很大。

