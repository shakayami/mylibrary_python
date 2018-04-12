def gcd(x, y):
    a = max([x, y])
    b = min([x, y])
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def lcm(x, y):
    return (x * y) // gcd(x, y)


def Primelist(N):
    Q = [True for i in range(N+1)]
    Q[0] = False
    Q[1] = False
    for i in range(2, N + 1):
        if Q[i] == True:
            for j in range(2 * i, N + 1, i):
                Q[j] = False
    P = []
    for i in range(N + 1):
        if Q[i]:
            P.append(i)
    return P


def PrimeFact(N):
    PF = []
    M = N
    k = 2
    while (True):
        od = 0
        if M % k == 0:
            while (True):
                if M % k == 0:
                    od += 1
                    M = M // k
                else:
                    break
            PF.append([k, od])
        else:
            k += 1
        if M == 1:
            break
    return PF


def Sigma(N):
    S = 1
    pf = PrimeFact(N)
    for a in pf:
        S = S * (a[0] ** (a[1] + 1) - 1) // (a[0] - 1)
    return S


def Phi(N):
    S = N
    pf = PrimeFact(N)
    for a in pf:
        S = (S * (a[0] - 1)) // a[0]
    return S


def Div(N):
    S = 1
    pf = PrimeFact(N)
    for a in pf:
        S = S * (1 + a[1])
    return S


def Rad(N):
    S = 1
    pf = PrimeFact(N)
    for a in pf:
        S = S * a[0]
    return S
