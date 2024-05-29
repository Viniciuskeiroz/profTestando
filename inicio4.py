simbolo_elemento = input("Digite a sigla do elemento químico: ")

simbolo_elemento = simbolo_elemento.capitalize()
print(simbolo_elemento)

if  simbolo_elemento == 'H':
    print("Número atômico: 1")
    print("Nome do elemento: Hidrogênio")
    print("Massa: 1")
elif simbolo_elemento == 'He':
    print("Número atômico: 2")
    print("Nome do elemento: Hélio")
    print("Massa: 4")
elif simbolo_elemento == 'Li':
    print("Número atômico: 3")
    print("Nome do elemento: Lítio")
    print("Massa: 6")
elif simbolo_elemento == 'O':
    print("Número atômico: 8")
    print("Nome do elemento: Oxigenio")
    print("Massa: 15,9")
else:
    print("Elemento não encontrado.")