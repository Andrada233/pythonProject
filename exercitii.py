def func(nr):
    fact=1
    if nr>1:
        for i in range(2,nr+1):
            fact *=i
        else:
            return 1
    print(fact)