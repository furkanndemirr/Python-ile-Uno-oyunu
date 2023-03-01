import random
import time

class Kartlar():

    def __init__(self,renk,desen):
        self.renk=renk
        self.desen=desen
    def __str__(self):
        return "{} {}\n".format(self.renk,self.desen)

def kasakart(b):
    i = 0
    while i < 1:
        a = random.choice(deste)
        b.append(a)
        deste.remove(a)
        print(a)
        i += 1
    return a

def kartçek():
    pass

def oyna(a,oy1,kartartı):

    if a.desen == "+2":
        print("+2 KARTINIZ VAR İSE ATINIZ.")
        i = 0
        o = 0
        t = 0
        while t < 2:
            e = random.choice(deste)
            kartartı.append(e)
            deste.remove(e)
            t += 1
        while i < len(oy1):
            if (oy1[i].desen == a.desen):
                print("Seçebileceğiniz kartın numarası:", i, "-->", oy1[i])
                o += 1
            i += 1
        if o != 0:
            x = int(input("SEÇECEĞİNİZ KARTIN NUMARASINI TUŞLAYINIZ...\n"))
            time.sleep(1)
            print(oy1[x])
            r = oy1[x]
            oy1.remove(oy1[x])
            return r
        else:
            print("ATABİLECEK KARTINIZ YOK KART ÇEKİNİZ...")
            time.sleep(1)
            t=0
            print(kartartı)
            while t<len(kartartı):
                oy1.append(kartartı[t])
                t+=1
            kartartı.clear()
    i=0
    o=0
    while i<len(oy1):
        if(oy1[i].desen==a.desen or oy1[i].renk==a.renk):
            print("Seçebileceğiniz kartın numarası:", i,"-->",oy1[i])
            o+=1
        i+=1
    if o!=0:
        x=int(input("SEÇECEĞİNİZ KARTIN NUMARASINI TUŞLAYINIZ...\n"))
        time.sleep(1)
        print(oy1[x])
        r=oy1[x]
        oy1.remove(oy1[x])
        return r

    else:
        print("ATABİLECEK KARTINIZ YOK KART ÇEKİNİZ...")
        time.sleep(1)
        e = random.choice(deste)
        oy1.append(e)
        print("Çektiğiniz kart", e)
        if(e.renk==a.renk or e.desen==a.desen):
            print(e)
            oy1.remove(e)
            deste.remove(e)
            return e
        else:
            print(a)
            deste.remove(e)
            return a
    if (len(oy1) == 0):
        return 0

renk = ["mavi","kırmızı","sarı","yeşil"]
desen = ["0","1","2","3","4","5","6","7","8","9","+2"]
deste=[]
for i in renk :
    for j in desen :
        deste.append(Kartlar(i,j))
oyuncu1=[]
oyuncu2=[]
kasa=[]
print("""
OYUN BAŞLIYOR...
-----------------
""")
time.sleep(1)
print("""
OYUNCU 1 KARTLAR :    
-------------------   
""")
i = 0
while i < 7:
    a = random.choice(deste)
    oyuncu1.append(a)
    deste.remove(a)
    print(a)
    i += 1
time.sleep(1)
print("""
OYUNCU 2 KARTLAR :    
-------------------   
""")
time.sleep(1)
i=0
while i < 7:
    b = random.choice(deste)
    oyuncu2.append(b)
    deste.remove(b)
    print(b)
    i += 1

print("""
OYUN BAŞLADI :    
-------------------   
""")
time.sleep(1)
kasa1=kasakart(kasa)

kartartı=[]
m=oyna(kasa1,oyuncu1,kartartı)

while True:
    print("Oyuncu2 oynuyor...")
    time.sleep(1)
    y=oyna(m,oyuncu2,kartartı)
    print("Oyuncu1 oynuyor...")
    time.sleep(1)
    m=oyna(y,oyuncu1,kartartı)
    if len(oyuncu2)==0:
        print("oyun bitti oyuncu 2 kazandı")
        break
    elif len(oyuncu1)==0:
        print("oyun bitti oyuncu 1 kazandı")
        break