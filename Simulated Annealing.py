import random
import math
x1,x2 = random.uniform(-10,10),random.uniform(-10,10)

t = 100000
tmin = 1
a = 0.999
def simulatedAnnealing(x1,x2):
	return (((4-((2.1*(x1**2)))+((x1**4)/3))*x1**2)+(x1*x2)+((-4+4*(x2**2))*(x2**2)))

def deltaE(awal,akhir):
	return akhir-awal

def probabilitas(awal,akhir,t):
	return (math.exp(-deltaE(awal,akhir)))

def perbandingan(current,new):
	if(new<current):
		return True
	else:
		return False
istate = simulatedAnnealing(x1,x2)
cstate = istate
while (t>tmin):
	for i in range (0,150):
		y1,y2 = random.uniform(-10,10),random.uniform(-10,10)
		newstate = simulatedAnnealing(y1,y2)
		if(perbandingan(cstate,newstate)==True):
			x1=y1
			x2=y2
			cstate = newstate
		else:
			if(random.random<probabilitas(cstate,newstate,t)):
				cstate=newstate
	
	t=t*a
print cstate