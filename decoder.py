def decode_pair(z):
	x, y = 0, 0
	while((z+1)%(2**x)==0):
		x+=1
	x-=1
	y=((z+1)/(2**x)-1)/2
	return int(x), int(y)

def decode_label(a):
	if(a==0):
		return ''
	L = ['A', 'B', 'C', 'D', 'E']
	c = L[a%len(L)-1]
	n = a//len(L) + 1	
	return f'{c}{n}'

def decode_var(c):
	if(c == 0):
		return 'Y'
	L = ['X', 'Z']
	ch = L[(c+1)%len(L)]
	n = (c+1)//len(L)
	return f'{ch}{n}'

def decode_state(b, var):
	if(b == 0):
		return f'{var} <- {var}'
	if(b == 1):
		return f'{var} <- {var} + 1'
	if(b == 2):
		return f'{var} <- {var} - 1'
	L = decode_label(b-2)
	return f'IF {var} != 0 Goto {L}'

def decode_instruction(I):
	a, x = decode_pair(z)
	b, c = decode_pair(x)
	# print(f'<{a},{x}>, x=<{b},{c}>')
	L = decode_label(a)
	var = decode_var(c)
	state = decode_state(b, var)
	if(L!=''):
		return f'[{L}] {state}'
	return state

if __name__=='__main__':
	while(True):
		z = int(input())
		print(decode_instruction(z))