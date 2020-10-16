# Entrada N - número inteiro de 1 até 2.147.483.647
# Converter N em binário
# Percorrer o vetor binário e ver qual o maior "gap"
# Gap é a quantidade de 0 entre 1 e 1. Ex: 10001 -> gap = 3 (3 zeros)

def decToBin(N):
    vet = []
    while(N > 0):        
        vet.append(N%2)
        N = N//2
    vet.reverse()
    return vet

def solution(N):
    maxGap = 0
    numZeros = 0
    binNumber = decToBin(N)

    for i in range(len(binNumber)):
        if(binNumber[i] == 1 and i != len(binNumber)-1):
            i = i + 1
            while(binNumber[i] != 1):
                numZeros = numZeros + 1
                if(i == len(binNumber)-1):
                    numZeros = 0
                    break
                else:
                    i = i + 1
            if(numZeros > maxGap):
                maxGap = numZeros
            numZeros = 0

    print(maxGap)
    #print(maxGap)
    print(*binNumber)

if __name__ == '__main__':
    N = 32
    solution(N)
    N = 1041
    solution(N)
    N = 529
    solution(N)
    
    #binNumber = decToBin(N)
    
