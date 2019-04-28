from numpy import *
import matplotlib.pyplot as plt
A = zeros([600,800])
for x in range(800):
    for y in range(600):
        zx=1.5*(x-800/2)/(0.5*1*800)
        zy=1.0*(y-600/2)/(0.5*1*600)
        i=255
        t=True
        while t==True:
            if zx*zx+zy*zy>=4:
                t=False
            if i<=1:
                t=False
            a=zx*zx-zy*zy-0.7
            zy=2.0*zx*zy+0.27015
            zx=a
            i=i-1
        A[y][x]=i
plt.imshow(A)
plt.show()
