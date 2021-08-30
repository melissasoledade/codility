
def solution(X, A):
    numbers = {}
       
    for i in range(0, len(A)):
        numbers[A[i]] = i
        if(len(numbers) == X):
            return i
    return -1       
   

if __name__ == '__main__':
    A = [1,3,1,4,2,3,5,4]
    print(solution(5, A))
    B = [1,3,1,4,2,3,4,2]
    print(solution(5, B))
