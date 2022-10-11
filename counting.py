#user inputs their favorite movie quote
counts = dict()
print('Enter your favorite movie quote')
line = input('')

words = line.split()
print('Words:', words)

#uses a dictionary to store and count freqency of words 
for w in words:
    counts[w] = counts.get(w,0)+1
print('Counts', counts)

#what word has most frequently occured  in the quote and how many times did it occur?
bigcount = None
bigword = None
for w,c in counts.items() :
    if bigcount is None or c > bigcount:
        bigword = w
        bigcount = c

print('The most common word is:', bigword)
print('Number of times the most common word occured:', bigcount)
