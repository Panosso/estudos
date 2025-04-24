#Create a code that receive a list with integer numbers and check only positive numbers and check with the first number that miss in the list.

def solution(A):

    A = sorted(list(set(A)))

    expect_value = 0

    if max(A) <= 0:
        return 1

    elif len(A) == 1:
        return A[0] + 1

    for i in range(0, len(A)):

        if A[i] > 0:

            expect_value = A[i] + 1

            if i < len(A)-1:

                if expect_value != A[i+1]:
                    return expect_value
                
            else:
                return A[i] + 1


print(solution([-1, -3, -4, 5, 6, 3, 2, 10, 32, 22, 1, 100]))
print(solution([7, 1, 3, 6, 4, 1, 2]))
print(solution([5, 6, 3, 2, 7, 8, 9, 1, 4]))
print(solution([-1]))
print(solution([0]))
print(solution([2]))
print(solution([1, 1, 1]))
print(solution([0, 0, 0]))
print(solution([1, 1, 1, 4, 2, 10]))
print(solution([-1, -1, -1]))
print(solution([-1, -2, -2, -3]))
