


# Report 1 : Population Growth Problems
### Author: Cathaya Liu ,   [*WHU*](http://physics.whu.edu.cn/)

***

## 一、问题描述
Population growth problems often give rise to rate equations that are first-order. For example, the equation 

![](http://latex.codecogs.com/gif.latex?\frac{dN}{dt}=aN-bN^2)

might describe how the number of individuals in a population, N, varies with time. Here the first term aN corresponds to the brith of new members, while the second term-bN^2 corresponds to deaths. The death term is proportional to N^2 to allow for the fact that food will become harder to find when the population N become large. Begin by solving the equation with b=0 using the Euler method, and compare your numerical result with the exact solution. Then solve the equation with nonzero values b . Give an intuitive explanation of you results. Interesting values of a and b depend on the initial population N . For small N(0) , a=10 and b=3 is a good choice, while for N(0)=1000 a good choice is a=10 and b=0.01 . 

## 二、问题分析
我们将分四个部分讨论这个问题。
* 求出该常微分方程在b=0情况下的解析解。
* 用Euler法求出该常微分方程在b=0情况下的数值解，并与其解析解进行比较。
* 用Euler法求出该常微分方程在b≠0情况下的数值解，尝试多个b的值并展示结果。
* 定性地解释结果。

## 三、算法设计及其Python实现
### I、程序分析
我们需要四个变量来描述这个数学模型，它们分别是：时间 t ，时间间隔（步长） Delta t ，当前人口数 N(t) 和初始人口数 N(0) 。

* 首先我们建立两个长度相同的独立一维数组，分别用来存放时间 t 和当前人口数 N(t) ，其元素一一对应。

* 对于时间 t 的数组，令其 t(0)=0 , t(n)=n\Delta t 。

* 对于人口数 N(t) 的数组，令其 N(0) 为初始人口数， N(t)= N(t-1)±f(N(t-1))\Delta t ，其中 f 取决于题目本身的变化。

* 循环生成时间 t 和当前人口数 N(t) 的数组元素。
* 画出 t-N 图。
### II、算法的Python实现
```
#引入matplotlib库

import matplotlib.pyplot as plt

#定义相关变量

N=[0 for x in range(0,'需要的长度')]
t=[0 for x in range(0,'需要的长度')]
N[0]='初始人口'
T='时间间隔'
t[0]=0

for i in range(1,'需要的长度'):
    N[i]=N[i-1]+f(N[i-1])*T
    t[i]=i*T

#绘图的相关设置

plt.title('')
plt.xlabel('t')
plt.ylabel('n')
P1=plt.plot(t,N)
plt.legend(handles = [P1], labels = [], loc = 'best')
plt.show()
```
## 四、程序的运行结果
### I、算法的试运行
首先我们尝试用该算法实现课本中的例子，即辐射衰变，以此检验算法的可靠性。

运行结果如下。
![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/Figure_1.png)

可以看到，该算法生成的图像和课本中所给的例子一致。因此初步判定该算法是有效的。
### II、常微分方程的解析解
当b=0时，该常微分方程的解析解可表述为：

![](http://latex.codecogs.com/gif.latex?N(t)=N(0)e^{at})
### III、b=0情形下解析解和数值解的对照
我们用两种不同的标记代表数值解和解析解，分别在不同的情形下探讨数值解的吻合程度。在以下模拟中N（0）均取1000.

首先我们来看当Delta t取0.05时的情况：
![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/fg1-3.png)
可以看到在步长为0.05时，误差比较大。因此我们缩小步长为0.01，效果如下：
![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/fg1-1.png)
上述两幅图都只模拟了10个点。当把模拟长度扩大到100个点时，效果如下：
![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/fg1-2.png)

可见，为了使模拟尽可能贴近真实情况，我们应该选取短步长，并模拟较少的点。
### IV、b≠0情形下的一些模拟
在b=0的情况下，不难看出这是标准的指数增长。但是由于实际情况下（诸如死亡、疾病、食物短缺）人口不可能按照这个模型增长，我们需要修改模型，引入一个衰减量。接下来我们将展示在不同情形下的模拟结果（并适度放飞自我）。

* 1、少量初始人口，短时间

![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/fg1-4.png)
可以看到这是一个类似于指数衰减的图像，即N^2项发挥主要作用。为了深入了解，我们看一下把时间延长一些会发生什么。
* 2、少量初始人口，长时间

![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/fg1-5.png)
有趣的事情开始出现了，N项和N^2项似乎达到了一个平衡（与黑恶势力达成共识.jpg）
* 3、放飞自我

题目中所说的【在初始人口足够少的时候，用b=3较好】。这个"足够小"大约是什么范围呢？
首先我们把N（0）设定为50，看看会发生什么。
![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/fg1-6.png)

emmmmm……笑容完全消失……这什么鬼！

为什么会这样呢……在N（0）为10的时候明明很和谐的。N（0）等于50就boom了……

我们选取一个中间值来跑一下：
![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/fg1-7.png)

可以看到已经发生了奇妙的变化。接下来我们再略微增加一下初始值……然后：
![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/fg1-8.png)
Boooooom!

由此可以推测，之所以会这个样子是因为过大的b值引起了人口值急剧的下滑，而我们的模型允许【负人口】和【非整数人口】……然后部分数据超出了Matplotlib的绘制范围，GG。
* 4、大量初始人口，短时间

当我们将N(0)设定为500，并按书上所说把b值调为0.01后，我们会得到这个：
![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/fg1-9.png)

看起来类似一条直线……把时间延长一些会如何呢？

* 5、大量初始人口，长时间

将时间延长十倍后我们得到了这个：
![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/fg1-10.png)
与黑恶势力再次达成共识.jpg

等等这个形状有点熟悉……这不是很像生物课本里种群增长的逻辑斯谛曲线吗！

可喜可贺，终于有一个比较正常的结果了。
## 五、未完待续
模拟人口增长是一件很好玩的事情……尤其是发现竟然能达到平衡的时候。这需要对N（0）、a和b的精确选择。接下来有时间大概会模拟一下不同a和b对模型的影响……以上！


