from pytube import YouTube as you
import os

#downloading the audio from the link
get_link=input('Please enter the link of the youtube audio : ')
song_link=you(get_link)
audio=song_link.streams.filter(only_audio=True).first()
mp4_file=audio.download()

#renaming the file as mp3 file 
name,ext=os.path.splitext(mp4_file)
new_file=name+'.mp3'
os.rename(mp4_file,new_file)

print('Downloaded : '+song_link.title)
