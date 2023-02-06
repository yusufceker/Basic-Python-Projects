import random

scr = 0
numgam = input("Kaç soru cevaplamak istersin?: ")

for Addition in range(int(numgam)):
    x = random.randint(10, 100)
    y = random.randint(10, 100)
    

    cevap = input(str(x) +(" + ") + str(y) + " = " )
    sa = int(cevap)
    oranlar = x + y
    if sa == oranlar:
        print("Doğru cevap")
        scr = scr + 1
    else:
        print("Yanlış!, Doğru Cevap " + str(oranlar))
        continue

print("Skorun " + str(int(scr)*100//int(numgam)) + "%")