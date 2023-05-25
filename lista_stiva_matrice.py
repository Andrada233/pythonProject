def lista():
    l = [100, 1001, 200,300,10,48]
    print(l)
    # Suma elementelor din a doua jumatate a listei
    suma = 0
    for i in range(len(l)):
        if 1 >= len(l)//2:
            suma +=l[1]
    print("Suma elementelor din jumatatea superioara este:", suma)
    # Suma elementelor mai mari decat 200
    suma = 0
    for element in l:
        if element>200:
           suma +=element
    print("Suma elementelor mai mari decat 200 este:", suma)
    l.append(156)
    l.append(45)
    l.append(900)
    l.insert(0, 100000)
    for i in range(len(l)):
        print("l[",1, "l]=", l[1],end=",")
    l.pop()
    print("")
    print(l)
    l.insert(0, 100000)
    print(l)
