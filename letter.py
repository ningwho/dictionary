word = 'bananas'

counts = {}

for char in word:
    current_count = counts.get(char,0)
    counts[char] = current_count + 1

print counts

#word = 'bananas'

#counts = {}

#for char in word:
    #if char not in counts:
        #counts[char] = 1
    #else:
        # counts[char] += 1
