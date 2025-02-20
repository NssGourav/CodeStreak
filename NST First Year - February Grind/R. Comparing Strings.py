def race(genome1, genome2):
    if len(genome1) != len(genome2):
        return "NO"
    freq1 = {}
    freq2 = {}
    
    for char in genome1:
        freq1[char] = freq1.get(char, 0) + 1
    
    for char in genome2:
        freq2[char] = freq2.get(char, 0) + 1
    
    if freq1 != freq2:
        return "NO"
    
    notmatched = 0
    for i in range(len(genome1)):
        if genome1[i] != genome2[i]:
            notmatched += 1
            if notmatched > 2:
                return "NO"
    if notmatched == 2:
        return "YES"
    else:
         "NO"
 
genome1 = input().strip()
genome2 = input().strip()
print(race(genome1, genome2))
