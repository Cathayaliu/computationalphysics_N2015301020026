# Report: Chaos in the Driven Nonlinear Pendulum
### Author: Cathaya Liu *2015301020026*
***
![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/5th%20homework/last.gif)
***
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
使用Euler-Cromer法计算
核心算法如下：
```
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
```
循环生成列表各元素，对θ做一判断，使之一直保持在[-π,π]范围内。
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

## 混沌系统对初值条件的敏感性

“一只蝴蝶扇动翅膀，就足以在遥远的地方引发一场暴风雨”。这句充满韵味的描述揭示了混沌系统第二迷人的性质（对初值条件的敏感性），而最迷人之处在于，混沌虽然不可预测，却依然有规律可循（我们会在下面吸引子的部分谈到这个）

那么，如何充分地展示这种敏感性呢？我们将从两个方面入手。

首先，我们将参数全部置于前述的默认值，取Δθ=0.001，将θ和θ+Δθ叠在一张图上：

![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/5th%20homework/dif%20xita0.png)
这样虽然比较直观，但并不能让我们对数值大小有比较清晰的认识，前面定义的Chaos.Compare函数大显身手。我们通过调用这个函数，可以直接画出Δθ-t的关系图：
![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/5th%20homework/dif%20xitac.png)
数值大小清晰地体现出来了……但我们希望能从中找到某种规律的影子，用对数坐标会不会好一点呢？
![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/5th%20homework/dif%20xital.png)

比之上图虽然好了一些，但仍然达不到课本上的那种效果，这也是需要改进之处。

## 吸引子与稳定性
到目前为止，混沌给我们的初始印象是非常【糟糕】的……这种似乎没有任何规律可言的系统，给人的感觉就像一只疯狂的兔子。令人欣慰的是，即使在如此混乱不堪的海洋里，也有安全的港湾。这就是吸引子。

所谓吸引子图，无非就是从上文中提到的θ-ω的关系图里选择一些特殊的点画出来。选择的条件是，在某些特定的时刻，F=0，即ΩD=2nπ。这在数学上很容易实现，但是在计算机模拟时，我们面临两个问题。第一，π是无理数；第二，我们模拟的时间步长是时间段，而非精确的时刻。这也就意味着我们必须取尽量小的步长，来削弱模拟的偏差。在下面的模拟中，我们的默认步长是0.008s。

先按照默认参数画图：

![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/5th%20homework/at0.png)

可以隐约感觉到什么，但是好像也没什么了不起的嘛……

还记得在前一节里，我们仅仅改变了θ的初值0.001，所带来的混乱吗？如过改变θ的初值0.001，吸引子又会如何呢？

![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/5th%20homework/at2.png)

不可思议的事情发生了……θ值在剧烈变动的同时，吸引子无动于衷。让我们改变一下步长，再看一遍：

![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/5th%20homework/at1.png)

依然是令人安心的稳定图样（图森破）……Amazing!

事实上，吸引子的倍周期增加正是通向混沌之路——由不动点到2周期振荡，4周期振荡，8周期振荡……周期不断地分叉，然后，混沌出现了。

本来还想画一个分叉图……能力有限，只能作罢。

## 什么会影响吸引子
在讨论这个问题之前，我对θ的初值大幅度改变会不会影响吸引子更有兴趣。

请看下图：

![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/5th%20homework/ac1.png)

答案显而易见，对于θ来说，吸引子是稳定的。

而对于F就不是这样了：

![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/5th%20homework/ac2.png)

此图搭配上面的“驱动力影响”图风味更佳。

可以得到一个直观的认识：混沌系统的吸引子分布较松散，且较复杂。而非混沌系统的吸引子则简单很多。

## 结论

非线性系统在合适的条件下会产生混沌。混沌对初值极度敏感，其随时间的演化不可预知。而混沌系统的吸引子则对初值条件不甚敏感，表现出很好的稳定性。吸引子的研究，是了解混沌本质的钥匙。

## 致谢和吐槽
* 印刷错误巨坑……P58正负号印反螺旋爆炸。
* 安利梅拉尼·米歇尔著《Complexity: A Guided Tour》，我的部分想法源于此书。
* 感谢我的电脑……跑几十遍300000+的循环，辛苦了ORZ

