def max_fibonacciness(test_cases):
    results = []
    for case in test_cases:
        a1, a2, a4, a5 = case
        a3_candidates = set([a1 + a2, a4 - a2, a5 - a4])
        max_fib = 0
        for a3 in a3_candidates:
            fib = 0
            if a3 == a1 + a2:
                fib += 1
            if a4 == a2 + a3:
                fib += 1
            if a5 == a3 + a4:
                fib += 1
            if fib > max_fib:
                max_fib = fib
        a3_pair1 = a1 + a2
        if a4 == a2 + a3_pair1:
            fib_pair1 = 2
            if a5 == a3_pair1 + a4:
                fib_pair1 += 1
            if fib_pair1 > max_fib:
                max_fib = fib_pair1
        a3_pair2 = a4 - a2
        if a5 == a3_pair2 + a4:
            fib_pair2 = 2
            if a3_pair2 == a1 + a2:
                fib_pair2 += 1
            if fib_pair2 > max_fib:
                max_fib = fib_pair2
        a3_pair3 = a5 - a4
        if a3_pair3 == a1 + a2:
            fib_pair3 = 2
            if a4 == a2 + a3_pair3:
                fib_pair3 += 1
            if fib_pair3 > max_fib:
                max_fib = fib_pair3
        results.append(max_fib)
    return results
 
t = int(input())
test_cases = []
for _ in range(t):
    a1, a2, a4, a5 = map(int, input().split())
    test_cases.append((a1, a2, a4, a5))
 
results = max_fibonacciness(test_cases)
 
for res in results:
    print(res)
