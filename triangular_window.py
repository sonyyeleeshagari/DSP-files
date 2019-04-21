import numpy as np
import matplotlib.pyplot as plt
m=int(input("enter m value:"))
h=[]
for n in range(0,m-1):
	x1=np.abs(n-(m-1)/2)
	w2=1-((2*x1)/(m-1))
	h=np.append(h,w2)
plt.plot(h)
plt.title("triangular window")
plt.xlabel("------>n")
plt.ylabel("------>w")
plt.show()
