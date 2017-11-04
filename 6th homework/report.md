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
