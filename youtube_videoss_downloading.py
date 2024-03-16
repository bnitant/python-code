from pytube import YouTube as you
import os

#downloading the video from the link
get_link=input('Please enter the link of the youtube audio : ')
video_link=you(get_link)
video=video_link.streams.get_highest_resolution()
mp4_file=video.download()

print('Downloaded : '+video_link.title)
