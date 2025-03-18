def robin_helps(test_cases):
    results = []
    for case in test_cases:
        n, k, a = case
        robin_gold = 0
        give_count = 0
        for gold in a:
            if gold >= k:
                robin_gold += gold
            elif gold == 0:
                if robin_gold > 0:
                    robin_gold -= 1
                    give_count += 1
        results.append(give_count)
    return results
t = int(input())
test_cases = []
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    test_cases.append((n, k, a))
 
results = robin_helps(test_cases)
for res in results:
    print(res)
