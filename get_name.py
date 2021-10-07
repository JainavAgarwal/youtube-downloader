import os
def extractnamewithoutext(s):
    str = ""
    st = ""
    t = 0

    for i in s:
        if(i=='.'):
            t = 1
            st = str
        if(t==0):
            st = str
        str = str+i
            
    return st
print(extractnamewithoutext("bjvn...webm"))
def fullname(path,name):
    ext = []

    
    fil = os.listdir(path)
    index = 0
    for i in fil:
        if(name==extractnamewithoutext(i)):
            ext.append(fil[index])
        index+=1
    if(ext==""):
        return ("No such file or directory")
    return ext
#path = "/Users/j/Movies"
#name = "12"
#print(fullname(path,name))

    


#os.chdir(os.getcwd())
#os.remove("QUIZ.pdf")
#path = "/Users/j/Desktop/jbn.jpeg";
#if os.path.exists(path):
#  os.remove(path)
#else:
#  print("The file does not exist")
#help(os)
#d = subprocess.call(f'/Users/j/Desktop/ffmpeg/ffmpeg -i input.webm out.mp4',shell=True)
#call = f'/usr/local/bin/ffmpeg -i input.webm out.mp4'# only supporte the same video_format, copy and not recode.
#print(d)
#print(os.getcwd())

#c = subprocess.call('ps -ax')
#print(c)
#o = os.system("Kill ")
#print(o)

