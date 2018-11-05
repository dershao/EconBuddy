def PA(i, N):
	return ((1+i)**N - 1)/(i * (1+i)**N)

def AP(i, N):
	return (i*((1+i)**N)/(((1+i)**N)-1)) 

def PF(i, N):
	return 1/((1+i)**N)

def AG(i, N):
	return 1/i - (N/((1+i)**N -1))

def FP(i, N):
	return (1+i)**N

def PAG(i, g, N):
	return (1 - (1+g)**N * (1+i)**(-N))/(i-g)

def AF(i, N):
	return i / ((1+i)**N -1)
        
