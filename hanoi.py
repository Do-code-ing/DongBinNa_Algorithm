n = int(input())
a = 1
b = 2
c = 3
def hanoi(n, a, b, c):
    global count
    if n <= 0:
        pass
    else:
        hanoi(n-1, a, c, b)
        print(a, c)
        hanoi(n-1, b, a, c)

def count(n):
    if n == 1:
        return n
    else:
        return count(n-1)*2+1

print(count(n))
hanoi(n, a, b, c)

# n = int(input())
# a = 1
# b = 3
# c = 2
# def hanoi(n, a, b, c):
#     global count
#     if n <= 0:
#         pass
#     else:
#         hanoi(n-1, a, c, b)
#         print(a, b)
#         hanoi(n-1, c, b, a)

# def count(n):
#     if n == 1:
#         return n
#     else:
#         return count(n-1)*2+1

# print(count(n))
# hanoi(n, a, b, c)