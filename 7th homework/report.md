# Report: The billiaed problem with different types of tables

### Author: Cathayaliu
***
## 题目描述
Study the behavior for other types of tables. One interseting possibility is a square table with a circular interior wall located either in the 
center, or slightly off center. Another possibility is an elliptical table.

## 算法描述

主要思路是将球的速度进行水平和竖直分解，然后在撞后使水平速度不变，竖直速度反向。核心代码如下：

```
for i in range(self.n):
    self.nextx = self.x[-1]+self.vx[-1]*self.dt
    self.nexty = self.y[-1]+self.vy[-1]*self.dt
    self.nextvx, self.nextvy = self.vx[-1], self.vy[-1]
    if self.nextx**2/3+self.nexty**2>1:
        self.nextx=self.x[-1]
        self.nexty=self.y[-1]
        while not(self.nextx**2/3+self.nexty**2>1):
            self.nextx=self.nextx+self.nextvx*self.dt/100
            self.nexty=self.nexty+self.nextvy*self.dt/100
        self.norm=np.array([self.nextx,3*self.nexty])
        self.norm=self.norm/np.sqrt(np.dot(self.norm,self.norm))
        self.v=np.array([self.nextvx,self.nextvy])
        self.v_perpendicular=np.dot(self.v,self.norm)*self.norm
        self.v_parrallel=self.v-self.v_perpendicular
        self.v_perpendicular=-self.v_perpendicular
        [self.nextvx,self.nextvy]=self.v_parrallel+self.v_perpendicular
    self.x.append(self.nextx)
    self.y.append(self.nexty)
    self.vx.append(self.nextvx)
    self.vy.append(self.nextvy)
```

## 程序运行结果

分别展示球在正圆和椭圆两种桌面下的运动情形：

正圆：

![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/7th%20homework/Figure_1-1.png)

椭圆：

![](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/7th%20homework/Figure_1-2.png)

## 结论
可以看出，球在正圆中有一障碍物的情况下，运动轨迹较为杂乱。而在无障碍物的情形下，则非常规则。
