MAXN = int(1e3+7)
MAXN = 5
X = [0]*MAXN
Z = [0]*MAXN
Y = [0]
last_occ = dict({'E':MAXN})

def decode_pair(z):
	x, y = 0, 0
	while((z+1)%(2**x)==0):
		x+=1
	x-=1
	y=((z+1)/(2**x)-1)/2
	return int(x), int(y)

def decode_label(a):
	if(a==0):
		return 'E'
	L = ['A', 'B', 'C', 'D', 'E']
	c = L[a%len(L)-1]
	n = a//len(L) + 1	
	return f'{c}{n}'

def decode_var(c):
	if(c == 0):
		return 'Y', 0
	L = ['X', 'Z']
	ch = L[(c+1)%len(L)]
	n = (c+1)//len(L)
	return ch, n

def if_instruction(var_name, var_index, label):
	var = 0
	if(var_name=='X'):
		var = X[var_index]
	elif(var_name=='Z'):
		var = Z[var_index]
	elif(var_name=='Y'):
		var = Y[0]
	
	if(var!=0):
		if(label in last_occ.keys()):
			return last_occ[label]
		else:
			return None
	return None

def instruct(var_name, var_index = 0, v = 0):
	if(var_name=='X'):
		X[var_index] += v
	elif(var_name=='Z'):
		Z[var_index] += v
	if(var_name=='Y'):
		Y[0] += v
	return None

def instruction(b, var_name, var_index):
	if(b == 0):
		return None
	if(b == 1):
		instruct(var_name, var_index, +1)
		return None
	if(b == 2):
		instruct(var_name, var_index, -1)
		return None
	L = decode_label(b-2)
	return if_instruction(var_name, var_index, L)


def apply_instruction(z, line):
	a, x = decode_pair(z)
	b, c = decode_pair(x)
	
	L = decode_label(a)
	last_occ[L] = line

	var_name, var_index = decode_var(c)
	go_to_state = instruction(b, var_name, var_index)

	if(go_to_state==None):
		return line+1
	return go_to_state


def snapshot(line, MAX_X, MAX_Z):
	print(line+1, end=' ')
	for i in range(1, MAX_X+1):
		print(X[i], end=' ')
	for i in range(1, MAX_Z+1):
		print(Z[i], end=' ')
	print(Y[0])

def initialize(z, line, MAX_X, MAX_Z):
	a, x = decode_pair(z)
	b, c = decode_pair(x)

	L = decode_label(a)
	last_occ[L] = line

	var_name, var_index = decode_var(c)
	if(var_name=='X'):
		MAX_X = max(var_index, MAX_X)
	if(var_name=='Z'):
		MAX_Z = max(var_index, MAX_Z)
	
	return MAX_X, MAX_Z


if __name__=='__main__':
	MAX_X, MAX_Z = 0, 0
	I = input().split(' ')
	for i in range(len(I)):
		I[i] = int(I[i])
		MAX_X, MAX_Z = initialize(I[i], i, MAX_X, MAX_Z)

	__input = input().split(' ')
	for i in range(len(__input)):
		X[i+1] = int(__input[i])

	line = 0
	while(line<len(I)):
		snapshot(line, MAX_X, MAX_Z)
		__line = apply_instruction(I[line], line)
		line = __line
		