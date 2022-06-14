#min 함수 사용하기
n, m = map(int, input().split())
small = []
for i in range(n)   :
    col = list(map(int, input().split()))
    small.append(min(col))
print(small)
print(max(small))