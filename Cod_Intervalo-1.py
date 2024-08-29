'''
Esta função verifica se um intervalo sobrepõe outro: por exemplo, se left 1 <= right2, significa que o menor valor do intervalo1 é maior ou igual a maior valor do intervalo 2,
portanto, possuem interseção e vice versa.  
'''
def verifica_intersecao(intervalo1, intervalo2):
    left1, right1 = intervalo1
    left2,right2 = intervalo2
    return left1<=right2 and left2<=right1 #retorna true caso exista intersecao


def imprimir_matriz(matriz):
    for linha in matriz:
        for elemento in linha:
            print(elemento, end=' ')
        print()


#intervalos = [[1,3], [2,5], [8,9], [4,6], [10,20]] #cria a lista de intervalos não necessariamente ordenados
intervalos = [[1,3], [2,9], [3,6], [2,4]]
intervalos_ordenados = [] #lista vazia que receberá a lista de intervalos ordenados
scd = [] #lista vazia que receberá os intervalos disjuntos
intervalos_ordenados = sorted(intervalos, key= lambda x: x[1]) # a função sorted ordena em ordem crescente


#M = [[]]
M = [[0 for _ in range(len(intervalos))] for _ in range(len(intervalos))]
for i in range(len(intervalos)):
    for j in range(len(intervalos)):        
        if (verifica_intersecao(intervalos[i],intervalos[j]) and (i != j)):
            M[i][j] = 1
            M[j][i] = 1


imprimir_matriz(M)


while intervalos_ordenados:
    menor_intervalo = intervalos_ordenados.pop(0) #apos ordenado, o menor intervalo é retirado da lista e adicionado em scd
    scd.append(menor_intervalo)
    
    intervalos_ordenados= [intervalo for intervalo  in intervalos_ordenados if not verifica_intersecao(menor_intervalo, intervalo)] # list comprehension
    '''
    caso o ultimo valor adicionado em scd NÃO tenha interseção com outro valor do intervalo, o intervalo sem interseção é mantido na lista intervalos_ordenados.
    Em seguida, após atualizar a lista  intervalos_ordenados, refaz todo o processo até que nao tenha mais nenhum valor a se verificar em numeros ordenados
    '''


print("Lista de intervalos SCD:")
print(scd)
quantidade = len(scd)
print("Existem %d coleções disjuntas na lista de intervalos fornecidas." %quantidade)
