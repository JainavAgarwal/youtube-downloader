def Convert(string):
    li = list(string.split("\n"))
    return li
file = open('audio.txt','r')
res = file.read()
file.close()
l = (Convert(res))
for i in l:
    print(i+"\n")
