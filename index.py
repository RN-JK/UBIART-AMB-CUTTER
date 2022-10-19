import os, json

setting=json.load(open('settings.json'))
codename=setting['mapName']
codenamelow=codename.lower()

mtrack=json.load(open('input/'+codenamelow+'_musictrack.tpl.ckd'))
startbeat=mtrack['COMPONENTS'][0]['trackData']['structure']['startBeat']
startbeat=abs(startbeat)
marker=mtrack['COMPONENTS'][0]['trackData']['structure']['markers'][startbeat]
timestamp=marker/48+setting['offset']
print('Making full audio of '+codename)
os.system('ffmpeg -y -ss "'+str(timestamp)+'ms" -nostats -loglevel 0 -i input/'+codename+'.'+setting['extension']+' output/'+codename+'.'+setting['extension'])

try:
    cine=json.load(open('input/'+codenamelow+'_mainsequence.tape.ckd'))
    for clip in cine['Clips']:
        if clip['__class']=='SoundSetClip':
            ambname=clip['SoundSetPath'].split('/')[-1].split('.')[0]
            if clip['StartTime']<=0:
                clip['StartTime']=abs(clip['StartTime'])
                print('splitting '+ambname)
                os.system('ffmpeg -y -ss "'+str(0)+'ms" -nostats -loglevel 0 -i input/'+codename+'.'+setting['extension']+' -t '+str(timestamp/1000)+' output/'+ambname+'.'+setting['extension'])
except:
    print('no cinematic for ambs...')