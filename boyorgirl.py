def main(p):
    x = set(p)
    if len(x) % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")
p = input().strip()
main(p)
