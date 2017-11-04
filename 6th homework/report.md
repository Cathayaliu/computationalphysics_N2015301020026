# Report: The Poincare sections & Bifurcation diagram
### Author: Cathayaliu  2015301020026
***
## 摘要
In this report, we fristly calculate some Poincare sections to check if our algorithm is correct. Then we plot the bifurcation diagram, using the parameters given in connection with Figure 3.10. At last, we make a magnified plot of the digram and estimate the Feigenbaum parameter.
## 算法介绍
本次报告采用的核心算法依然是Euler-Cromer方法。之前看到陈洋瑶学姐用了四阶Runge-Kutta方法，估摸了下计算量，还是算了吧ORZ……似乎闻到了CPU的香气。

上次蔡老师提醒我注意一下吸引子图的问题……比起课本范例和其他一些同学的图，我的似乎“稀疏”很多，也不那么光滑。这是因为点的选取方式不同。之前的思路是，先循环生成ω数组和θ数组，然后按照**固定**间隔取点，由于π是个无理数，而ΔT无法取成无限小，所以误差会累积，最后的结果也就Boom了。

为了避免误差的累积，我对取点的部分做了修正。采用动态筛选法，在循环中直接判断是否需要取点，最后得到了较好的结果。

核心代码部分如下：
```
for j in range(0,300):
    FD=1.35+0.0005*j
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
        if (t[i+1]>900*math.pi)and((OMGD*t[i+1])/(2*math.pi)-int((OMGD*t[i+1])/(2*math.pi))<(OMGD*T)/(2*math.pi)):
            D.append(θ[i+1])
            F.append(FD)
```
这是一个循环嵌套，第一个循环用来遍历1.35-1.5之间的F值（间隔为0.0005），第二个循环对每个特定的F值生成ω列表和θ列表，并按照*“周期数大于300，与F同相”*的条件选取点，添加到名为D的列表中。

## 尝试与对比：The Poincare sections
为了展示新的取点方式的优越性，我们用新方法和之前的方法画一些Poincare sections，进行对照。
* 原方法：

![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/5th%20homework/at0.png)

* 新方法

![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/6th%20homework/KS.png)

可以看到新方法的效果好很多。

## 绘制分岔图
接下来我们绘制分岔图，先按照课本上的参数，F从1.35-1.5

![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/6th%20homework/C223.png)

可以看到比较明显的分岔。

然后出于好奇，我尝试着绘制了更大范围的F，得到了下面的图：

![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/6th%20homework/over.png)

Emmmmm……或许这就是混沌吧.jpg

请特别注意这张图上1.26-1.3之间的部分。书上提到，周期的倍增最后通向混沌，而1.26-1.3似乎是……周期倍减，系统由混沌重归秩序。或者看起来有这个意思。

## the Feigenbaum parameter

通过对上图进行局部放大并记录分岔点，我得到了如下表格：

|F1|F2|F3|
|-|-|-|
|1.424|1.459|1.475|

计算后有：δ=2.1875……这和δ ≈4.669差距较大。但是目前绘图的精度只能到这一步了。只能说，一个图的精度啊，不仅需要个人的努力，也要考虑到计算机的性能。

