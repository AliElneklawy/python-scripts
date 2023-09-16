from moviepy.video.io.VideoFileClip import VideoFileClip
import re
import os
     
input_video_path = input('Path to the video file: ')
timestamps_file = input('Path to the timestamps file: ')
pattern = r'([\d:]+)[\s-]+(.+)'
timestamps_scnds = []
video_clip = VideoFileClip(input_video_path)

with open(timestamps_file, 'r') as f:
    lines = f.readlines()
lines = ''.join(lines)

matches = re.findall(pattern, lines)
timestamps, chapter_names = zip(*matches)

ts = list(timestamps)
chapter_names = list(chapter_names)

for i in range(len(chapter_names)):
    chapter_names[i] = re.sub(r'[^\w\s-]', ' ', chapter_names[i])
    chapter_names[i] = re.sub(r'\s+', ' ', chapter_names[i])

for i in range(len(ts)):
    ts[i] = ts[i].strip()
     
    if len(ts[i].split(':')) == 2:
        ts[i] = '00:' + ts[i]
    
    splitted = ts[i].split(':')
    hrs, mins, scnds = int(splitted[0]), int(splitted[1]), int(splitted[2])
    total_scnds = hrs * 60 * 60 + mins * 60 + scnds
    timestamps_scnds.append(total_scnds)

for i, start in enumerate(timestamps_scnds):
    if i < len(timestamps_scnds) - 1:
        end = timestamps_scnds[i + 1] 
        fname = f"{i+1}- {chapter_names[i]}.mp4"
        output_path = os.path.join(os.path.dirname(input_video_path), fname)

        if not os.path.exists(output_path):
            sub_clib = video_clip.subclip(start, end)
            sub_clib.write_videofile(output_path, audio_codec='aac', fps=60)

end = timestamps_scnds[-1]
fname = f"{len(timestamps_scnds)}- {chapter_names[-1]}.mp4"
output_path = os.path.join(os.path.dirname(input_video_path), fname)
if not os.path.exists(output_path):
    sub_clib = video_clip.subclip(timestamps_scnds[-1])
    sub_clib.write_videofile(output_path, audio_codec='aac', fps=60)

video_clip.reader.close()
video_clip.audio.reader.close_proc()
