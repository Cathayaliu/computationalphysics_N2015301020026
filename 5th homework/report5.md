# Report: Chaos in the Driven Nonlinear Pendulum
### Author: Cathaya Liu *2015301020026*

## 前言
本周我们学习了计算物理的第三章，对于Chaos这个主题期待已久~因此想尽可能多地改变一下相关参数，看能不能得到一些有趣的结果。这次报告不会针对课后作业的某个具体问题，而是对所有问题都有涉及。比起具体的问题，我更喜欢讨论“泛用”的方法。
## 摘要
本次我打算涉及的主题有：
* 绘制θ-t, ω-θ的关系图
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
* 第一个函数的功能是返回一个二维列表，列表中包含有θ、ω的全部信息以及绘制吸引子图所需要的全部信息。
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
现在，我们可以把这个函数当成一本手册来使用。如果你需要ω，你只需要输入Chaos.Chaos_Cathaya('相关参数')[0]；同理，如果你需要θ，你只需要输入Chaos.Chaos_Cathaya('相关参数')[1]；你可能注意到，我们的返回值里还有ωa和θa这两个列表，我们稍后会解释它们的作用。

* 第二个函数专门用来计算Δθ,通过对第一个函数的调用，较为简洁地完成了这个任务。
```
    def Chaos_Compare(DIF,FD,OMGD,LIM,L,Q,xita):
        
        Dθ=[0 for x in range(0,LIM)]
        Dθ[0]=DIF
        
        for i in range(0,LIM):
            Dθ[i]=Chaos.Chaos_Cathaya(FD,OMGD,LIM,L,Q,xita+DIF)[1][i]-Chaos.Chaos_Cathaya(FD,OMGD,LIM,L,Q,xita)[1][i]
            
        return Dθ
```
第二个函数和第一个函数的参数相差无几，仅仅多了一个参数DIF，它用来表示θ初始情况的差值。比如，两个θ在刚开始的时候只相差0.01，那么我们就令DIF=0.01。

* 我们画的很多图中都需要时间t作为横坐标，而仅仅是为了时间t去调用第一个函数实在是太没有效率了。因此我专门定义了下面这个函数，用来提供绘图所需的时间标度。
```
    def Timeline(LIM,T):
        
        t=[0 for x in range(0,LIM)]
        t[0]=0
        
        for i in range(0,LIM-1):
            t[i+1]=t[i]+T
            
        return t
```
## 绘制θ-t, θ-ω的关系图

在经过了上面一连串冗长的定义和循环后，接下来终于可以舒服一点了。

现在，想要绘制θ-t，你只需要敲入区区一行代码：
```
plt.plot(Chaos.Chaos_Timeline('相关参数'),Chaos.Chaos_Cathaya(相关参数)[1])
```
同样地，你也只需要区区一行代码绘制ω-θ：
```
plt.scatter(Chaos.Chaos_Cathaya('相关参数')[1],Chaos.Chaos_Cathaya('相关参数')[0],s='你想要多大的点')
```
你可能注意到了，绘制θ-t的时候我用了plot指令，而绘制ω-θ的时候我用了scatter指令。至于为什么要这样做，猜猜看~

只靠上面的一堆代码是没有说服力的，为了检验它的正确性，我们不妨带入课本里的参数跑一下，看结果如何。
![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/5th%20homework/demo2.png)
![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/5th%20homework/demo1.png)

可见我们的程序工作的还不错。

## 驱动力、空气阻力因子、绳长对θ的影响
*除了需要探讨的变量外，我们做如下约定：F=1.2，Ω=2/3，L=9.8，q=0.5,θ初值为0.2。*

#### 驱动力带来的影响

我们选取一系列的F值，分别作图：
![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/5th%20homework/dif%20f.png)
当F为比较小的值时，如我们所料，并没有混沌现象出现。当F等于1时，我们可以注意到图形开始出现明显的扭曲。但是当F足够大时（F=6），系统似乎又具有了某种规律。这是比较令人费解的。

#### 空气阻力因子带来的影响

同样地，我们选取一系列的q值，分别作图：
![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/5th%20homework/dif%20q.png)
和F的情况相反，当q因子比较小时，系统才具有混沌性。而当q足够大时（q>0.6），系统便失去了混沌性。

#### 绳长带来的影响

课本上把绳长取9.8，使其与重力加速度比值为一，这个取值很耐人寻味。那么，不一样的绳长会带来什么变化呢？
![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/5th%20homework/dif%20l1.png)
较短的绳子在我们所给的条件下摆动相当规律，而当L大于5后，情况发生了很大变化。但是，和F很相似，当L足够大时，系统似乎重新变得“规整”了。为了充分表现这一点，我用更长的时间模拟了L=9.8和L=40两种情形：
![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/5th%20homework/dif%20l2.png)
可以清晰地看出，L=9.8时，增加时间的长度并不会让运动具有某种规律性。而L=40时，在经历了初始的混乱后，系统重新变得“规整”了。
