# <문제> 문자열 재정렬: 문제 설명
# 알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어집니다.
# 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.
# 예를 들어 K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력합니다.

n = "K1KA5CB7"
n = "AJKDLSI412K4JSJ9D"
answer = ""
num = 0
n = sorted(n)
for c in n:
    if c.isalpha():
        answer += c
    else:
        num += int(c)
if num != 0:
    answer += str(num)
print(answer)

# [문제 해결 아이디어]
# 요구 사항대로 충실히 구현
# 문자열이 입력되었을 때 문자를 하나씩 확인합니다.
#   - 숫자인 경우 따로 합계를 계산합니다.
#   - 알파벳의 경우 별도의 리스트에 저장합니다.
# 결과적으로 리스트에 저장된 알파벳을 정렬해 출력하고, 합계를 뒤에 붙여 출력하면 정답입니다.

# 해답
data = "K1KA5CB7"
data = "AJKDLSI412K4JSJ9D"
result = []
value = 0
for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)
result.sort()
if value != 0:
    result.append(str(value))
print("".join(result))