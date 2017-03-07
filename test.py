n= eval(input('Digiteumnumero: '))
lista = []
for i in range(2,n+1,2):
    lista = [i] + lista
print(lista)