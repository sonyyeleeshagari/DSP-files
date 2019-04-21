import numpy as np
import matplotlib.pyplot as plt
m=int(input("enter m value:"))
h=[]
pi=3.14
for n in range(0,m-1):
	w3=0.5*(1-np.cos((2*pi*n)/(m-1)))
	h=np.append(h,w3)
plt.plot(h)
plt.title("hanning window")
plt.xlabel("------>n")
plt.ylabel("------>w")
plt.show()

