# [재귀 함수]
# 재귀 함수(Recursive Function)란 자기 자신을 다시 호출하는 함수를 의미합니다.
# 단순 형태의 재귀 함수 예제
def aaa():
    print("본인을 호출했어요")
    aaa()
# aaa()
# RecursionError: maximum recursion depth exceeded while calling a Python object
# 컴퓨터 메모리에 스택과 같이 함수가 쌓여, 빠르게 메모리가 가득차서 문제가 발생할 수 있어, 제한이 있다.
# 그렇기에 재귀 제한을 느슨하게 만드는 방법을 사용하거나, 스택 객체를 따로 만들어서 그것을 이용하는 방법도 있다.

# 재귀 함수를 문제 풀이에 사용할 때는 재귀 함수의 종료 조건을 반드시 명시해야 합니다.
# 종료 조건을 제대로 명시하지 않으면 함수가 무한히 호출될 수 있습니다.
#   - 종료 조건을 포함한 재귀 함수 예제
def recursive_function(i):
    if i == 100:
        return
    print(i, "번째 재귀함수에서", i+1,"번째 재귀함수를 호출합니다.")
    recursive_function(i+1)
    print(i, "번째 재귀함수를 종료합니다.")
# recursive_function(1)
# 스택에 데이터를 넣은 것처럼 사용하는 결과를 보여준다.

# 팩토리얼 구현 예제
# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

print("반복적으로 구현:", factorial_iterative(5))
print("재귀적으로 구현:", factorial_recursive(5))

# 최대공약수 계산(유클리드 호제법) 예제
# 두 개의 자연수에 대한 최대 공약수를 구하는 대표적인 알고리즘
# 유클리드 호제법
#   - 두 자연수 A, B에 대하여 (A>B) A를 B로 나눈 나머지를 R이라고 합시다.
#   - 이때 A와 B의 최대공약수는 B와 R의 최대 공약수와 같습니다.
# 이것을 재귀 함수로 작성할 수 있습니다.
def gcd(a, b):
    # a, b = max(a,b), min(a,b) # 혹시몰라 정렬
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b) # 이 과정에서 알아서 큰수와 작은수로 정렬됨
print(gcd(12, 20))

# 재귀 함수를 잘 활용하면 복잡한 알고리즘을 간결하게 작성할 수 있습니다.
#   - 단, 오히려 다른 사람이 이해하기 어려운 형태의 코드가 될 수 있으므로 신중하게 사용해야 합니다.
# 모든 재귀 함수는 반복문을 이용하여 동일하 기능을 구현할 수 있습니다.
# 재귀 함수가 반복문 보다 유리한 경우도 있고 불리한 경우도 있습니다.
# 컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택 프레임에 쌓입니다.
#   - 그래서 스택을 사용해야 할 때 구현상 스택 라이브러리 대신에 재귀 함수를 이용하는 경우가 많습니다.
# DFS에서는 재귀 함수를 이용한다.