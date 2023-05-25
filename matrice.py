def suma_matrice():
    #partea de initializare a variabilelor/constantelor
  n = 4
  sdp =0
  sds =0
  matrice = [[0]*n for _ in range (n)]

  for i in range(n):
      for  j in range(n):
        print(i,"",j, end= "=")
        matrice [i] [j] = int(input())
        if i < j:
            sdp += matrice[i] [j]
        if i+j<n - 1: #inseamna ca elementul meu este deasupra diagonalei secundare
            sds +=matrice [i] [j]
        print("Suma d p=", sdp)
        print("Suma d p=", sds)


if __name__  == "__main__":
    suma_matrice()