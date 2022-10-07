#practice for splicing strings
str = 'X-DSPAM-Confidence: 0.8475'
pos = str.find('0')
print(pos)
piece = str[pos:]
num = float(piece)
print(num)
