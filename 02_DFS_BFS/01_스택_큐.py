# [스택 자료구조]
# 먼저 들어온 데이터가 나중에 나가는 형식(선입후출)의 자료구조입니다.
# 입구와 출구가 동일한 형태로 스택을 시각화할 수 있습니다.
# DFS 알고리즘뿐 만아니라 다양한 알고리즘에서 사용된다.

# 스택 동작 예시
# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()

stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) # 최상단 원소부터 출력
print(stack) # 최하단 원소부터 출력


# [큐 자료구조]
# 먼저 들어온 데이터가 먼저 나가는 형식(선입선출)의 자료구조입니다.
# 큐는 입구와 출구가 모두 뚫려 있는 터널과 같은 형태로 시각화 할 수 있습니다.

# 큐 동작 예시
# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()

# 리스트를 사용하여 해도 되지만, 시간복잡도가 조금 더 걸리기에
# 덱 라이브러리 사용이 좋다.
from collections import deque

queue = deque()

queue.append(5)
print(queue)
queue.append(2)
print(queue)
queue.append(3)
print(queue)
queue.append(7)
print(queue)
queue.popleft()
print(queue)
queue.append(1)
print(queue)
queue.append(4)
print(queue)
queue.popleft()

print(queue)
queue.reverse()
print(queue)
print(list(queue))

# 스택 자료구조는 들어온 순서에서 마지막 것만 제거하면 되기 때문에 자료의 인덱스의 변화가 없다.
# 그렇기에 list를 사용하여 스택 구조를 만들어 사용해도 된다.
# 그러나 큐 자료구조에서는 제일 먼저 들어온 것을 제거하기 때문에 리스트로 자료구조를 만들 경우,
# 인덱스 변화가 일어나기 때문에 시간 복잡도가 조금 더 걸린다.
# 그렇기에 덱 라이브러리를 이용하여 popleft를 하는 것이 시간 복잡도 측면에서 좋다.
# (리스트에서 pop과 덱에서 popleft의 시간복잡도는 같은듯하다.)