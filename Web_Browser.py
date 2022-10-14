import urllib.request, urllib.parse, urllib.error

fan = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fan:
    print(line.decode().strip())



