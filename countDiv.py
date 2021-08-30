def solution(A, B, K):
    array = list(range(A, B+1))
    div = 0

    if(K == 1):
        return (B-A+1)
    
    for i in range(0, len(array)):
        if(array[i] % K == 0):
            div = div + 1        
    return div
    
if __name__ == '__main__':
    print(solution(6, 11, 13))