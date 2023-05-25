
# Sa se scrie o functie care sa calculeze diferenta dintre cel mai mare si cel mai mic dintre cele 3 numere citite de la tastatura
def dif_max_min(*args):
    maxim = max(*args)
    minim = min(*args)
    print(maxim-minim)

# Sa se scrie o functie care primeste ca parametrii un numar intreg si determina semnul sau
def semn():
    if n >0:
       print('Pozitiv')
    elif n == 0:
        print('Nul')
    else:
        print('Negativ')

#Intr o clasa sunt F fete si B baieti. Fiecare fata citeste 3 pagini pe zi si fiecare
#baiat citeste 2 pagini pe zi. Cate pagini vor citi copii in n zile?Citeste de la tastaura nr F B n . Va afisa
# nr de pagini citite
def sir(F,B,n):
    f = F*3*n
    b = B*2*n
    print(F,B,n)

# Sa se scrie un program care citeste o propozitie si determina numarul de cuvinte din propozitie care incepe
# si se termina cu o vocala


#Se da un sir de caractere repr. un cuvant. Sa se afiseze lista prefixelor si lista sufixelor cuvantului dat.
def sir():
    cuvant=''
    for i in range (0,len(cuvant)):
        if i == 0:
            def nr_natural():
                suma = 0

#Să se scrie un program care citește numărul natural n și determină suma S=2+4+..+(2n).
n=0
S = int(input)
S =n*(n+1)
print('Suma calculata este', S)

#Să se scrie un program care citește numărul natural n și determină valoarea lui n!.
n = int(input())
n_factorial=1
for i in range(n,n+1):
    n_factorial = n*i
print(n_factorial)

#Gigel în timp ce așteptă să meargă la doctor se joacă cu noul lui telefon. A observat ca atunci când este
# pe ecranul de start și apasă pe o tastă numerică se aude o notă muzicală.

#Dar lui i-a venit ideea să codeze fiecare notă muzicală în acest mod: Nota do1 cu numărul 0
#Nota re cu numărul 1 Nota mi cu numărul 2 Nota fa cu numărul 3 Nota sol cu numărul 4
#Nota la cu numărul 5 Nota si cu numărul 6 Nota do2 cu numărul 7
muzica =''
do1:'0'
re :'1'
mi : 2
fa : 3
sol : 4
la : 5
si : 6
d02 : 7
suma = 0
n= int(input())
note = input().split('')
for note in muzica:
    suma += note.get(note)
    suma %=8
    print(muzica)

#Într-un şir de numere naturale se numeşte vârf un element care are doi vecini şi este strict mai mare decât aceştia.
#Se dă un şir cu n elemente, numere naturale. Calculaţi suma elementelor din şir care sunt vârfuri.

n = int(input())
list.nr=[]
for i in range(1,n+1):
    list.nr = (map(int,input().strip().split,''))

# Pe    poarta  unei    fabrici  ies   în ordine n pachetefiecare având  un   volum  cunoscut.Pachetele  sunt  transportate  folosind  camioane
#Toate   camioanele au  aceeași  capacitate C, iar procedura este următoarea:
#fiecare pachet scos din fabrică este imediat încărcat într-un camion, și nu este posibil ca la încărcare să fie mai mult de un camion.

def pb():
    n = int(input)
    s = 0
    putere = 1

def pb():
    minim = 1
    x = 'c'
    n = input.split()
    for i in range (len(n)):
        if x-int(n[i]) < 0:



