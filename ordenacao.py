# ÉRICO ROSISKI WEBER E FLÁVIO
# MÉTODOS DE PESQUISA E ORDENAÇÃO - UFN - 2019
# 30.10.2019
# CASO QUEIRA REALIZAR A ESCRITA DO RESULTADO EM CSV ESTE ENCONTRA-SE NO CODIGO COMENTADO, BASTA DESCOMENTAR

import csv

def cocktailSort(Mylist): 
    print('Ordenando por cocktailSort')
    n = len(Mylist) 
    swapped = True
    start = 1
    end = n-1
    cont = 0
    while (swapped == True):    
        swapped = False
        for i in range (start, end): 
            if (Mylist[i][9] > Mylist[i + 1][9]) : 
                Mylist[i], Mylist[i + 1]= Mylist[i + 1], Mylist[i]            
                swapped = True
        if (swapped == False): 
            break
        end = end-1
        for i in range(end-1, start-1, -1): 
            if (Mylist[i][9] > Mylist[i + 1][9]): 
                Mylist[i], Mylist[i + 1] = Mylist[i + 1], Mylist[i] 
                swapped = True
        start = start + 1
  
def insertionSort(Mylist1): 
    print('Ordenando por insertionSort')
    for i in range(1, len(Mylist1)): 
        key = Mylist1[i] 
        key1 = Mylist1[i][9]
        j = i-1
        while j >=0 and key1 < Mylist1[j][9] : 
                Mylist1[j+1] = Mylist1[j] 
                j -= 1
        Mylist1[j+1] = key 


f = open('listings.csv',  encoding="utf8")
csv_f = csv.reader(f)
Mylist=[]
Mylist1=[]

for row in csv_f:
    Mylist.append(row)

Mylist1 = Mylist


while(1):
    print('Digite 1 para ordenar a lista utilizando CocktailSort e 2 para ordenar utilizando InsertionSort. A coluna preço será ordenada')
    a = int(input())
    if(a==1):
        cocktailSort(Mylist) 
        for i in range(len(Mylist)): 
            print(Mylist[i]) 
        with open("ordenado.csv",'w') as result_file:
            wr = csv.writer(result_file, dialect='excel')
            for i in range(len(Mylist)):
                wr.writerow(Mylist[i])
    elif(a==2):
        insertionSort(Mylist1)
        for i in range(len(Mylist1)): 
            print(Mylist1[i]) 
        with open("ordenado.csv",'w') as result_file:
            wr = csv.writer(result_file)
            for i in range(len(Mylist1)):
                wr.writerow(Mylist1[i])
    else:
        print('Opção nao encontrada')    
    print("CSV Ordenado de acordo com o critério price (PREÇO), coluna 9:") 


# for i in range(len(Mylist1))
# with open("ordenado.csv",'w') as result_file:
#     wr = csv.writer(result_file, dialect='excel')
#     for i in range(len(Mylist)):
#         wr.writerow(str(Mylist[i]))