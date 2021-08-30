
def solution(X, A):
    numbers = list(range(1, X+1)) # creates array from 1 to X + 1
    time = 0
       
    for i in range(0, len(A)):
        try:
            numbers.remove(A[i])
            time = i
        except:
            pass
        if(len(numbers) == 0):
            return time
    return -1       
   

if __name__ == '__main__':
    A = [1,3,1,4,2,3,5,4]
    print(solution(5, A))
    B = [1,3,1,4,2,3,4,2]
    print(solution(5, B))
