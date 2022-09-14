from moviepy.editor import *
start = float(input("Start (in seconds): "))
end = float(input("End (in seconds): ")) 
path = input("Enter the path: ")
clip = VideoFileClip(path)
clip = clip.subclip(start, end)
clip.write_videofile(r"edited.mp4")
