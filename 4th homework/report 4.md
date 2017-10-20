# Report 4: Throwing A Baseball
![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/4th%20homework/bangqiu.png)
***
## 摘要
在学习过计算物理的2.4节后，我决定尝试这做这样一件事情：模拟一个任意初始速度的球，并查看它在Y和Z两个方向上的轨迹。在这个模拟中，我希望引入尽可能多的自定义参数，以便于对比各种参数对轨迹的不同影响。现在的可变参数有：初始速度，发射角度，空气阻力相关参数，球的自旋速度，以及模拟的时间长度。在接下来的完善中，我将为这个模拟添加气压随高度变化带来的影响，以及球的速度变化对空气阻力造成的影响。

## 程序设计和算法描述
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
