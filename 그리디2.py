n, m, k = map(int, input().split()) 
a=list(map(int, input().split()))

a= list(reversed(sorted(a)))    #리스트를 내림차순으로 정렬
print(a)

index = 0                   #인덱스 변수
sum=0                       #결과에 쓰일 합계
for i in range(1, m+1)   :  
    if i%(k+1) == 0 :   #초과할 때 리스트에서 두번째로큰 요소에 접근
        index=1         
    sum+=a[index]       #더해주기
    index=0
    print(sum)

print("finial", sum)




#[sol.2]
# from numpy import true_divide


# n, m, k =map(int, input().split())
# data = list(map(int, input().split()))

# data.sort()

# first = data[n-1]
# second = data[n-2]

# result =0

# while 1 :
#     for i in range(k)   :
#         if m ==0 :
#             break
#         result += first
#         m-=1
#     if m ==0 : 
#         break
#     result += second 
#     m-=1

# print(result)



#sol.3  (m이 매우 커질 때 빠르게 계산하기 위한 알고리즘)

# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))

# data.sort()
# first = data[n-1]
# second = data[n-2]

# count = int(m/(k+1)) *k     #큰 수가 더해지는 횟수 계산
# count += m%(k+1)

# result = 0
# result += count * first     #가장 큰 수 더하기
# result += (m-count) *second #두번 째 큰 수 더하기

# print(ResolutionError)






