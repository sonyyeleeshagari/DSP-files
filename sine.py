##!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
f1=2
fs=60
sa=100
n=np.arange(sa)
c=np.sin(2*np.pi*n*f1/fs) #first sine signal
plt.figure(1)
plt.xlabel('time period')
plt.ylabel('Amplitude')
plt.subplot(311)
plt.stem(n,c)
plt.show()
