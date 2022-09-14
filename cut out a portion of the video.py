
from moviepy.editor import *


start = float(input("Start: "))
end = float(input("End: ")) 
path = input("Enter the path: ")
clip = VideoFileClip(path)
clip = clip.subclip(start, end)
clip.write_videofile(r"edited.mp4")