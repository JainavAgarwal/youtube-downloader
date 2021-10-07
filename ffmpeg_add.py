import os
import subprocess


def removefile(path,file):
    if os.path.exists(file):
        os.remove(file)

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

def extractvideoname(video):
    x = 0
    y = 0
    str = ""
    for i in video:
        if(x>=5):
            return extractnamewithoutext(video[y:len(video)])
            #return str
        if(i=='ÿ' or i=='Ǆ' or i=='ϔ' or i=='Ӝ' or i=='अ'):
            x+=1
        else:
            x=0
        y+=1      
    
        
def addaudio(path,video,audio,name):
    file1 = open("name1.txt","w")
    file1.write(str(audio)+"\n"+str(video)+"\n")
    file1.close()
    na = name
    vi = video
    aud = audio
    ffmpeg = "'/Users/Nole/Desktop/Youtube-downloader/ffmpeg'"
    #ffmpeg -i video.mp4 -i audio.wav -map
    # 0:v -map 1:a -c:v copy -shortest output.mp4
    video = "'"+video+"'"
    audio = "'"+audio+"'"
    name = "'"+path+"/"+name
    command = ffmpeg+" -i "+video+" -i "+audio+" -map 0:v -map 1:a -c:v copy "
    command = command + "-shortest " + name + ".mp4'"
    print(command)
    t = subprocess.call(command,shell=True)
    print(t)
    removefile(path,vi)
    removefile(path,aud)
    
    
