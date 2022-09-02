import os
from re import search
from natsort import natsorted

subtitle = []
video = []
dir_name = input("Enter the path: ")
files_in_directory = os.listdir(dir_name)

for file in files_in_directory:
	if file.endswith(".srt") or file.endswith(".ass") or file.endswith(".sub"):
		subtitle.append(file)
	elif file.endswith(".mp4") or file.endswith(".mkv"):
		video.append(file)

try:
	subtitle.sort(key=lambda x: x[(search(r'[Ee][0-9]{1,2}', x).span()[1])-1])	#sort based on episode number
	video.sort(key=lambda x: x[(search(r'[Ee][0-9]{1,2}', x).span()[1])-1])
except:
	subtitle = natsorted(subtitle)
	video = natsorted(video)

matching = list(zip(video, subtitle))
for renaming in matching:
		if renaming[0].endswith(".mkv"):
			vid_file = renaming[0].removesuffix(".mkv")
		elif renaming[0].endswith(".mp4"):
			vid_file = renaming[0].removesuffix(".mp4")
		if renaming[1].endswith(".srt"):
			try:
				os.rename(f"{dir_name}\{renaming[1]}", f"{dir_name}\{vid_file}.srt")
			except:
				continue
		elif renaming[1].endswith(".ass"):
			os.rename(f"{dir_name}\{renaming[1]}", f"{dir_name}\{vid_file}.ass")
		elif renaming[1].endswith(".sub"):
			os.rename(f"{dir_name}\{renaming[1]}", f"{dir_name}\{vid_file}.sub")
		
		