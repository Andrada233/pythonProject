def cautaresir(sirprincipal,subsir):
    i=0
    n = len(sirprincipal) - len(subsir)
    while i<=n:
        j = 0
        while j<=len(subsir):
            if sirprincipal [j+i]!= subsir[j]:
                j = j+1
                break
            else:
                j = j+1
            if j == len(subsir):
                return 1
            i = i+j
        return -1

def adunarerec(n):
    if n == 1:
        return 1
    return n + adunarerec(n-1)

def factorial(n):
    f = 0
    t1 = 0
    t2 = 1
    for i in range(2,n+1):
        f = t1+t2
        t1 = t2
    return f

#Fibonacci recursiv
# F(n) =
def fibrec(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibrec(n-1) + fibrec(n-2)

# de realizat o functie recursiva care imi determina numarul de aparitii al cifrei 0 intr-un numar natural
 # n este un numar natural