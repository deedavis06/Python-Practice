counts = dict()
print('Enter your favorite famous line from a movie')
line = input('')

words = line.split()
print('Words:', words)

for w in words:
    counts[w] = counts.get(w,0)+1
print('Counts', counts)

bigcount = None
bigword = None
for w,c in counts.items() :
    if bigcount is None or c > bigcount:
        bigword = w
        bigcount = c

print('The most common word is:', bigword)
print('Number of times the most common word occured:', bigcount)