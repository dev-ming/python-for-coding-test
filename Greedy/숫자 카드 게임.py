n, m = map(int, input().split())

result = 0

for i in range(n):
    data = map(int, input().split())
    min_value = min(data)
    result = max(min_value, result)

print(result)
