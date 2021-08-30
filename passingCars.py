def prefix_sums(A):
    n = len(A)
    P = [0] * (len(A)+1)

    for i in range(1, len(A)+1):
        P[i] = P[i-1] + A[i-1]    
    return P

def count_total(P, x, y):
    return P[y+1] - P[x]

def solution(A):
    ones = 0
    passing = 0
    for i in range(len(A)-1, -1, -1):
        if(A[i] == 1):
            ones = ones + 1
        else:
            passing = passing + ones
        
        if(passing > 1000000000):
            return -1
    return passing

if __name__ == '__main__':
    A = [0,1,0,1,1]
    print(solution(A))

   
    

