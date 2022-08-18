import os

srt = []
mkv_or_mp4 = []
dir_name = input("Enter the path: ")
files_in_directory = os.listdir(dir_name)

for file in files_in_directory:
	if file.endswith(".srt") or file.endswith(".ass"):
		srt.append(file)
	elif file.endswith(".mp4") or file.endswith(".mkv"):
		mkv_or_mp4.append(file)


matching = zip(mkv_or_mp4, srt)
for renaming in list(matching):
		#srt_file = renaming[1].removesuffix(".srt")
		#os.rename(f"{dir_name}\{renaming[0]}", f"{dir_name}\{srt_file}.mkv")
		vid_file = renaming[0].removesuffix(".mkv")
		os.rename(f"{dir_name}\{renaming[1]}", f"{dir_name}\{vid_file}.srt")