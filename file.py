#1
def nr_natural():
   p = 0
   for i in range(n):
       if i == 8:
           print("Apare cifra 8", )
           p = p*8


#2
def matrice_patratica():
    n  = 4
    sdp = 1
    for i in range(n):
        for j in range(n):
            if i == j:
               s = i+j

#3
def dictionar():
    litere =0
    list = ('a','b','c','d','e','f','g','h','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    diet = {}
    for i in range(len(litere)):
        dict [litere[i]] = litere[1].upper + ''+ str(i+1)
# rezolvare
n = input() #orice se citeste de la tastatura =  input
e = 0
p = 1
c=0
for e in n:
    if e == '8':
        c +=1
        if int(e)%2 == 1:
            p = p*int(e)

if __name__ == "__main_":
    nr_natural()