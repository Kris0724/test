file=open("./dict.txt")

d = {}
#d['kris'] = 100
#d['amy'] = 99.9

#print d['kris']

while 1:
    line = file.readline()
    if not  line:
        break
    line = line.strip('\n')
    arr = line.split(',')
    #print arr[0],arr[1]
    d[arr[0]] = float(arr[1])

print d
