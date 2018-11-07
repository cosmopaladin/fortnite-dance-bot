import io, sys, os, glob, subprocess, time, random

# 600 sections in 10 minutes
vid_list = glob.glob('*.mp4')
while True:
    video_num = random.randint(0, len(vid_list)-1)
    try:
        subprocess.run(['vlc', vid_list[video_num], '--play-and-exit'], timeout = 600)
    except subprocess.TimeoutExpired:
        pass
