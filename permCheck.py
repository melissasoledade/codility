
def solution(A):
    max_num = max(A)
    #len(A) == max_num
    
    if(len(A) == max_num and sum(A) == int(max_num*(max_num + 1) / 2) and len(A) == len(set(A))): # somatório de 1 até N
        return 1
    else:
        return 0

if __name__ == '__main__':
    print(solution([4,3,1]))