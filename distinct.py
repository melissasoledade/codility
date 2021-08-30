def set_solution(A):
    return len(set(A))

def solution(A):
    A.sort()
    dif = 0

    if(len(A) == 0):
        return 0

    for i in range(1, len(A)):
        if(A[i] != A[i-1]):            
            dif = dif + 1
    return dif + 1
    
if __name__ == '__main__':
    A = [2,1,1,2,3,1]
    #print(set_solution(A))
    print(solution(A))
#contar quantos números diferentes tem no array

[1,1,1,2,2,3]