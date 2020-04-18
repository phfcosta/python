lista = [1,3,7,"thiago macedo",23,14]
print(lista)
lista.append("python")
print(lista)
lista.append(20)
print(lista)
print(lista.index("thiago macedo"))
print(lista.index(20))
print(lista.count(14))
lista.remove("python")
print(lista)
lista.reverse()
print(lista)

lista2 = [1,9,4,2,3,7]
lista2.sort()
print(lista2)