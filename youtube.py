from pytube import YouTube
import datetime
import json

#conver list to dictionary
def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct

#down load function
def yt_videos(url):
    yt = YouTube(url)

    # get video url to download
    stream_all = yt.streams.filter(progressive=True, file_extension='mp4').all()
    resolutions = []
    for stream in stream_all:
        resolutions.append(stream.resolution)
        resolutions.append(stream.url)
    resolutions_dict = Convert(resolutions)

    #get audio
    audio_all = yt.streams.filter(only_audio=True).all()
    audio_list = []
    for audio in audio_all:
        audio_list.append(audio.abr)
        audio_list.append(audio.url)
    audio_dict = Convert(audio_list)
   
    # show on display json format
    x = {
        "ID" : yt.video_id,
        "Title" : yt.title,
        "Publish Date" :str(yt.publish_date),
        "Lenght" : str(datetime.timedelta(seconds=yt.length)),
        "Thumbnail URL" : yt.thumbnail_url,
        "Download" : {
            "Video" : resolutions_dict,
            "Audio" : audio_dict
        }
    }
    y = json.dumps(x)
    return y