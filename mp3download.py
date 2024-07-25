from pytubefix import YouTube
from pytubefix.cli import on_progress
 
youtube_link = "http://youtube.com/watch?v=2lAe1cqCOXo"
 
yt = YouTube(youtube_link, on_progress_callback = on_progress)
print(yt.title)
 
ys = yt.streams.get_audio_only()
ys.download(mp3=True, filename="audio") # pass the parameter mp3=True to save in .mp3