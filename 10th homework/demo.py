import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


the_origin_V=[[0 for col in range(65)] for row in range(65)]
for i in range(15,49):
    the_origin_V[20][i]=1
    the_origin_V[44][i]=-1
'''
the_origin_V[0][1]=0.67
the_origin_V[6][1]=0.67
the_origin_V[0][5]=0.67
the_origin_V[6][5]=0.67
the_origin_V[0][2]=0.33
the_origin_V[6][2]=0.33
the_origin_V[0][4]=0.33
the_origin_V[6][4]=0.33
'''
    
V=[the_origin_V]

for i in range(0,30):
    VO=V[i]
    K=[[0 for col in range(65)] for row in range(65)]
    Delta_V=0
    for i in range(1,64):
        for j in range(1,64):
            if (VO[i][j]!=1 and VO[i][j]!=-1):
                K[i][j]=round((VO[i-1][j]+VO[i+1][j]+VO[i][j-1]+VO[i][j+1])/4,2)  
                Delta_V+=abs(VO[i][j]-K[i][j])
    for i in range(0,65):
        for j in range(0,65):
            K[i][j]=K[i][j]+V[0][i][j]
    V.append(K)

x=[]
for i in range(0,65):
    x.append([i for j in range(65)])
X=sum(x,[])

y=[]
for i in range(0,65):
    y.append([i for i in range(0,65)])
    
Y=sum(y,[])
Z1=sum(V[14],[])
Z5=sum(V[15],[])

fig = plt.figure(figsize=(12,6))
ax1 = fig.add_subplot(121,projection='3d')
ax2 = fig.add_subplot(122,projection='3d')
ax1.scatter(X,Y,Z1,s=2)

ax2.scatter(X,Y,Z5,s=2)

plt.show()