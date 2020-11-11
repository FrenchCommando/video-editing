import os
from moviepy.editor import VideoFileClip

folder = "MoreGoproBike"
video_input = os.path.join(folder, "GOPR5761.MP4")
video_output = os.path.join(folder, "video_output8.mp4")


with VideoFileClip(video_input) as source_video:
    with source_video.speedx(factor=8) as sped_up_video:
        sped_up_video.write_videofile(video_output)
