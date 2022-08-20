from time import sleep
from moviepy.editor import VideoFileClip
import os

path = input("Enter the path: ")
files_in_path = os.listdir(path)
only_vids = []
for vids in files_in_path:
	if vids.endswith('.mp4') or vids.endswith(".mkv"):
		only_vids.append(vids)

duration = 0

for file in only_vids:
	clip = VideoFileClip(f"{path}\{file}")
	duration += clip.duration
	clip.close()

print(f"{round(duration/60/60, 2)} hours")
sleep(5)