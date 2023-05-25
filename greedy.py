def spectacol(lista):
    lista=0
    final = [lista[0]]
    ultimaora = lista [0] [1]
    for spec in lista:
        if spec[0] >= orasfarsit:
            final.append(spec)
            orasfarsit = spec[1]
    print(final)
    print("Numar spectacole este:", len(final))

def rucsac(inv, gmax):
    bag=0
    bag = sorted(bag, key=lambda k:k [1]/k[0], reverse=True)
    r = [] #continutul rucsacului
    g = 0 #greutatea lui
    val = 0 #valoarea rucsacului
    for el in bag:
          if g + el[0]<=gmax:
              r.append(el)
              g = g+ el[0]
              val= val+el[1]
          else:
              fract= gmax-g
              if fract+ g<= max and fract>0:
                  r.append(fract, fract*el)
                  g = g + el[1]
                  val = val+fract*el//el[0]
    print(r,g,val)


if __name__=="__main__":

    spectacol()

    # specs = list