##!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
f1=20
f2=40
f3=600
sa=100
n=np.arange(sa)
c=np.sin(2*np.pi*n*f1/f3) #first sinusoidal signal
plt.subplot(311)
plt.xlabel('time period')
plt.ylabel('Amplitude')
plt.stem(n,c)
plt.show()
d=np.sin(2*np.pi*n*f2/f3) #second sinusoidal signal
plt.subplot(312)
plt.xlabel('time period')
plt.ylabel('Amplitude')
plt.stem(n,d)
plt.show()
e=c+d
plt.subplot(313)
plt.xlabel('time period')
plt.ylabel('Amplitude')
plt.plot(n,e)
plt.show()
