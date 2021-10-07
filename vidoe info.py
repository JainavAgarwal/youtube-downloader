from __future__ import unicode_literals
import json
import youtube_dl
ydl_opts = {}
link = input('Enter the link')
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    meta = ydl.extract_info(link
        ,download=False,
        ie_key=None, extra_info={}, process=True, force_generic_extractor=False)
length  = len(meta['entries'])
for i in range(length):
    print(((meta['entries'])[i])['title'])
file1 = open("info.txt","w")
file1.write(str(meta))
file1.close()
'''form = meta['formats']
#print("Size\tID\tFormat\tExt\tResolution")
for x in form:
    print(type(x))
    for y,z in x.items():
        print(y," : ",z)
        print("\n")'''
    
    #print(str(round(x['filesize']/1048576,2))+"Mb\t"+
     #     str(x['format_id'])+"\t"+str(x['format'])+"\t"+str(x['ext'])+"\t"+str(x['thumbnails']))
#1024*1024 = 1048576'''
    
