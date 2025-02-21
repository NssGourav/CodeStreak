def string(k, s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    string = ""
    for char in freq:
        if freq[char] % k != 0:
            return "-1"
        string += char * (freq[char] // k)

    return string * k

k = int(input().strip()) 
s = input().strip()      
print(string(k,s))
