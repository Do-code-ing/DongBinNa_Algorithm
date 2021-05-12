# <문제> 거스름 돈: 문제 설명
# 거스름 돈 500원, 100원, 50원, 10원 무한대
# 손님에게 거슬러주어야 할 돈이 N원일 때, (N은 10의 배수)
# 거슬러 주어야할 동전의 최소 개수를 구하시오.

N = 1260
array = [500, 100, 50, 10]
count = 0
for coin in array:
    count += N // coin
    N %= coin
print(count)

# [정당성 분석]
# 가지고 있는 동전 중에서 큰 단위가 항상 작은 단위의 배수이므로
# 작은 단위의 동전들을 종합해 다른 해가 나올 수 없기 때문입니다.