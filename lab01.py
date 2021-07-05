#You Need to install 
	#pip install numpy
	#https://numpy.org/install/

	#pip install matplotlib
import numpy as np
import matplotlib.pyplot as plt
w = 4
h = 3
d = 400
x_List=[]
y_List=[]
n= int (input ("Enter the No of data"))
print("\n\n X axis Input \n\n\n")
for i in range (0,n):
	ele=input()
	x_List.append(ele)



print("\n\n\n Y axis input \n\n")
for i in range (0,n):
	yinput=input()
	y_List.append(yinput)



x=np.array(x_List)
y=np.array(y_List)
m,c=np.polyfit(x,y,1)
#print("Y = ",round(m,4) ,"X +",round(c,4))
print("Y = ",m ,"X +",c)
plt.figure(figsize=(w, h), dpi=d)
plt.plot(x, y)
plt.savefig("out.png")