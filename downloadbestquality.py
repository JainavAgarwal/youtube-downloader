from __future__ import unicode_literals
import youtube_dl
from ffmpeg_add import *
#from get_name import *
def downloadbest(link,path):
    vid = 0
    video = []
    audio = []
    best = ""
    def getfilecontent():       
        file1 = open("name.txt","r")
        res = file1.read()
        file1.close()
        removefile(os.getcwd(),"name.txt")  # from ffmpeg_add
        return res
    
    def my_hookaudio(d):
        if(d['status']=='finished'):
            fileaud = open("audio.txt","a")
            fileaud.write(str(d['filename'])+'\n')
            fileaud.close()   
        file1 = open("name.txt","w")
        file1.write(d['filename'])
        file1.close()
    def my_hookvideo(d):
        if(d['status']=='finished'):
            filevid = open("video.txt","a")
            filevid.write(str(d['filename'])+"\n")
            filevid.close()
        file1 = open("name.txt","w")
        file1.write(d['filename'])
        file1.close()
        #if d['status'] == 'finished':
        #print('Done downloading, now converting ...')

    best = 'bestaudio/best'
    key = 'ÿǄϔӜअ'   #so that i can extract the dimensions of the video easily
    captionofsavedvideo = "/"+key+"%(title)s %(height)sx%(width)s.%(ext)s"
    
    ydl_opts = {
        'outtmpl':path+captionofsavedvideo,
        'format': best,       
        'noplaylist' : True,        
        'progress_hooks': [my_hookaudio],  
    }
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

    audio = getfilecontent()
    best = 'bestvideo/best'
    ydl_opts = {
        'outtmpl':path+captionofsavedvideo,
        'format': best,       
        'noplaylist' : True,        
        'progress_hooks': [my_hookvideo],  
    }
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
        #info_dict = ydl.extract_info(link, download=False)
        #video_url = info_dict.get("url", None)
        #video_id = info_dict.get("id", None)
        #name = info_dict.get('title', None)
    
    video = getfilecontent()
    name = extractvideoname(video)  #name with the dimensions of the video
    addaudio(path,video,audio,name)
    #files = fullname(path,name)
    #print(files)
    #print(" audio = "+audio+" video = "+video)
#addaudio(path,)


