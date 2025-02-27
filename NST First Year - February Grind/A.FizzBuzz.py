def Fizzbuzz(n):
    one_cycle = n // 15
    result = one_cycle * 3
    remainder = n % 15
    for i in range(remainder + 1):
        if i % 3 == i % 5:
            result += 1

    return result
t = int(input())
for _ in range(t):
    n = int(input())
    print(Fizzbuzz(n))

#First we checked one complete cycle is divisible by 15 or not 
# then we choice to nultiply with 3
#then we have divided with 15 as the remainder should be a part of 3 *5 
#then if the number is in the range of 0 to remainder and is divisble by 3 and 5 then increasing the count by 1
#then we can return result
