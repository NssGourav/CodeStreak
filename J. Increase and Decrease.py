n = int(input())
a = list(map(int, input().split()))
total_sum = sum(a)
if total_sum % n == 0:
    print(n)
else:
    print(n - 1)
