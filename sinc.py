##!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
a=np.arange(-10,10,0.1)
x=np.sinc(a)
plt.title('sinc function')
plt.xlabel('time period')
plt.ylabel('Amplitude')
plt.subplot(311)
plt.plot(a,x)
plt.show()
