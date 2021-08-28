'''
An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

def solution(A)

that, given an array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].
'''
def binarySearch(A, k):
    pass

 # dado i de 1 até len(A) + 1
 # buscar i em A
 # se não achar, retorna elemento i 
 # se achar, incrementa i e busca próximo

def solution(A):
    ordered_A = sorted(A)
    limit = len(A) + 1
    i = 1
    element = binarySearch(A, i)  
   
    while(element == -1 and i <= limit):
        i = i + 1
        element = binarySearch(A, i)

    return element

if __name__ == '__main__':
    A = [2,3,1,5]
    print(solution(A))