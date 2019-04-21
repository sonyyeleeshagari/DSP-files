import numpy as np
import matplotlib.pyplot as plt
m=int(input("enter m value:"))
h=[]
pi=3.14
for n in range(0,m-1):
	x=np.cos((2*pi*n)/(m-1))
	w4=0.54-((0.46)*x)
	h=np.append(h,w4)
plt.plot(h)
plt.title("hamming window")
plt.xlabel("------>n")
plt.ylabel("------>w")
plt.show()

