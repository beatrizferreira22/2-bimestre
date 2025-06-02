numero = (5, 8, 12, 8, 7, 8, 3)
#para ser uma tupla precisa estar entre parenteses!
print("tupla original:", numero)
#imprimindo para o usuario a tupla original, sem manipulações
print("tamanho da tupla:", len(numero))
print("acessando pelo indice",numero[2])
#escolhendo qual sera mostrado atraves do indice, lembrando começa do zero
print("fazendo um slicing do 2 ao 5", numero[2:5])
#o slicing ele nao pega o ultimo item definido no recorte
print("quantas vezes o numero 8 repete", numero.count(8))
print("posição da primeira ocorrencia do numero 7: ", numero.index(7))
minimo_tupla = min(numero)
print("menor numero dentro da tupla", minimo_tupla)
maximo_tupla = max(numero)
print("maior numero dentro da tupla", maximo_tupla)
sum_tupla = sum(numero)#soma da tupla
print(sum_tupla)
sorted_tupla = sorted(numero)#ordena a tupla
print(sorted_tupla)
print("o numero 4 está na tupla??", 4 in numero)
numero2=(15,20)
tupla_concatenada=numero+numero2
print("a concatenação das tuplas 1 e 2 resulta na nova tupla:", tupla_concatenada)
tupla_duplicada=numero*2
print(tupla_duplicada)
