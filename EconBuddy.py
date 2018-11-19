'''
EconBuddy ver 1.0 beta
Open in idle: F5 to run or exec(open("/path/to/EconBuddy.py").read())
Open in terminal: python3 -i EconBuddy.py, control + D or quit() or exit() to exit
'''


def PA(i, N):
    '''Series Present Worth Factor: PA(percentage, years)'''
    i /= 100
    return ((1 + i)**N - 1) / (i * (1 + i)**N)


def AP(i, N):
    '''Capital Recovery Factor'''
    i /= 100
    return (i * ((1 + i)**N) / (((1 + i)**N) - 1))


def PF(i, N):
    '''Present Worth'''
    i /= 100
    return 1 / ((1 + i)**N)


def AG(i, N):
    '''Gradient Arithmetic'''
    i /= 100
    return 1 / i - (N / ((1 + i)**N - 1))


def FP(i, N):
    '''Future Worth (Compound Amount Factor)'''
    i /= 100
    return (1 + i)**N


def PAG(i, g, N):
    '''Geometric Series Present Worth'''
    i /= 100
    return (1 - (1 + g)**N * (1 + i)**(-N)) / (i - g)


def AF(i, N):
    '''Sink Fund Factor'''
    i /= 100
    return i / ((1 + i)**N - 1)


def ROI(NPW, investment):
    '''Return of investment: ROI(Net Present Worth, investment) in percentage'''
    return (NPW / investment) * 100

def twoDP(number):
    '''round to two decimal point'''
    return round(number, 2)

def CTF(t, d, i):
    '''Capital Tax Factor with half-year rule applied
    CTF(tax rate, depreciation rate(CCA), interest rate)'''
    t/=100
    d/=100
    i/=100
    return 1 - (t * d * (1 + i / 2)) / ((i + d) * (1 + i))

def CSF(t, d, i):
    '''Capital Salvage Factor'''
    t/=100
    d/=100
    i/=100
    return 1 - (t * d) / (i + d)

def CIIR(ireal, inflat_rate):
    '''Combined Interest Inflation Rate'''
    ireal/= 100
    inflat_rate/=100
    return (1+ireal)*(1+inflat_rate) - 1 
