

dt = 0.001
minA = 1
maxA = 2

def mod(x):
	if x >= 0:
		return x
	else:
		return -x

def bestA(data):
	minSum = 0
	ans  = 1
	l  = len(data)
	a = minA
	while a <= maxA:
		sum = 0
		for i in range(0,l):
			sum = sum + mod(data[i] - a**i)*i
		if minSum == 0 or sum < minSum:
			minSum = sum
			ans = a
		a = a + dt
	print("Best Exponent Constant is - " + str(ans) + "With avg minSum = " + str(minSum/l)) 
	return ans