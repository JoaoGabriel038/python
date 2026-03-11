inimigos = [(50, 30), (100,100), (10,90), (30,50)]

x = int(input("informe a coordenada para arriscar:"))
y = int(input("informe a coordenada para arriscar:"))

if (x, y) in inimigos:
    inimigos.remove((x, y))
    print("acertou inimigo")
else:
    print("errou")