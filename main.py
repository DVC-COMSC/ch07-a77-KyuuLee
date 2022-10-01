num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))
N = len(num1) 
M = len(num2) 

minlen = N if N <= M else M
num3 = [] 
for i in range(minlen):
	num3.append(num1[i])
	num3.append(num2[i])

# if N == minlen:
# 	num3 += num2[minlen:]
# else:
# 	num3 += num1[minlen:]

num3 += num2[minlen:] if N == minlen else num1[minlen:]


print (num3)
