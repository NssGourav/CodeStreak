for _ in range(int(input())):
    num = int(input())
    count = 0
    
    for div in range(1, num + 1):
        if num % div:
            break
        count += 1
    
    print(count)
