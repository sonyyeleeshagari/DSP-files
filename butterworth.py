import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
from pylab import *
x=float(input("enter the passband gain="))
y=float(input("enter the stopband gain="))
wp=float(input("enter wp in rad/sec="))
ws=float(input("enter ws in rad/sec="))
p=np.log(((1/x**2)-1)/((1/y**2)-1))
q=np.log(wp/ws)
N=0.5*(p/q)
print(N)
a=((1/x**2)-1)
b=(0.5/N)
c=(a**b)
wc=wp/c
print(wc)
s=np.arange(0,100,10)
f=1/((1+((s/wc)**(2*N)))*0.5)
plt.plot(s,f)
plt.show()
l=[]
for k in range(0,N)
	m=np.2*sin((2*k+1)*np.pi/2*N)
	l.append(m)




