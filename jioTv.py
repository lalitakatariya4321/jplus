import requests;
import json;

global allChannels
m3ustr = ''

apiUrl="https://fox.toxic-gang.xyz/jplus/key/$ToReplace"


with open("jiodata.json", "r") as savedChannelDetailInFile:
    savedChannels = json.load(savedChannelDetailInFile)
allchannels=savedChannels



for channelList in allchannels:
        print(channelList['channel_id'])
        response = requests.request("GET",apiUrl.replace("$ToReplace",str(channelList['channel_id'])))
        jsonResult= response.json()
        streamUrl=jsonResult[0]['data']['initialUrl']
        hdntl=jsonResult[0]['hdntl']
        clearKeys=str(jsonResult[0]["keys"])
        channelLogo= "https://jiotv.catchup.cdn.jio.com/dare_images/images/"+channelList['logoUrl']
        extvlcopt="#EXTVLCOPT:plaYtv/7.1.5 (Linux;Android 13) ExoPlayerLib/2.11.7\n"
        kodiProps= '#KODIPROP:inputstream.adaptive.license_type=clearkey\n'+'#KODIPROP:inputstream.adaptive.license_key='+clearKeys.replace("'",'"')+'\n'
        extHttp= '#EXTHTTP:{"Cookie":"'+hdntl+'"}\n'
        m3ustr += "#EXTINF:-1 "
        m3ustr += "tvg-id="+ "\"" + str(channelList['channel_id']) + "\" " + "group-title=" + "\"" + channelList['channelCategoryId'] + "\" " "tvg-logo=\""+channelLogo+ "\"," + channelList['channel_name'] +"\n"+ kodiProps + extHttp +extvlcopt+streamUrl+'|Cookie:'+hdntl+"\n\n"


with open("allChannelPlaylist.m3u", "w") as allChannelPlaylistFile:
        allChannelPlaylistFile.write(m3ustr)
