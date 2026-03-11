lista = []

#inserir novos elementos
lista.append("teste inserção")

#mostrando a lista inteira
print(lista)

#mostrando elemento pelo indice
print(lista[0]) #primeiro indice
print(lista[-1]) #ultimo indice
print(lista[0:3]) #até

#exibindo com loop
for valor in lista:
    print(valor) #cada volta "valor" assume o proximo valor da lista

#removendo
lista.pop() # remove o ultimo valor
print(lista)
lista.remove("1") # remove o valor selecionado
print(lista)

#tamanjho da lista
print(len(lista)) #mostra quantos elementos