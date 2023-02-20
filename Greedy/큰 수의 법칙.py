import time
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

starttime = time.time()

data.sort()
first = data[-1]
second = data[-2]

# 내 코드
# result = 0

# while (m):
#     for i in range(k):
#         result += first
#         m -= 1
#     result += second
#     m -= 1

# 답 코드 -> 큰 수가 더해지는 횟수를 계산
count = int(m/(k+1))*k
count += m % (k+1)

result = 0
result += (count) * first
result += (m-count)*second

print("result", result)

endtime = time.time()
a = endtime-starttime
print(a)
