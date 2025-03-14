n = int(input())
ticket = input().strip()

half = n
first_half = list(ticket[:half])
second_half = list(ticket[half:])

first_half_sorted = sorted(first_half)
second_half_sorted = sorted(second_half)
less_than = True 
greater_than = True  
for i in range(half):
    if int(first_half_sorted[i]) >= int(second_half_sorted[i]):
        less_than = False  
        break
for i in range(half):
    if int(first_half_sorted[i]) <= int(second_half_sorted[i]):
        greater_than = False  
        break
if less_than or greater_than:
    print("YES")
else:
    print("NO")
