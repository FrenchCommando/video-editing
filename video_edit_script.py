import os
import datetime
from moviepy.editor import VideoFileClip, AudioFileClip, ImageClip, TextClip, \
    concatenate_videoclips, CompositeVideoClip
from moviepy.video.tools.drawing import circle
from moviepy.editor import vfx


folder = "coinamant"

audio_input = "audio.webm"

video_inputs = [
    "GOPR6194.MP4",
    "GP016194.MP4",
    "GOPR6195.MP4",
    "GOPR6196.MP4",
    "GOPR6197.MP4",
    "GOPR6198.MP4",
    "GP016198.MP4",
]

audio_clip = AudioFileClip(os.path.join(folder, audio_input)).subclip(t_end=-4)
print(f"Audio duration {audio_clip.duration}"
      f"- {datetime.timedelta(seconds=audio_clip.duration)}")

video_clip = concatenate_videoclips([
    VideoFileClip(os.path.join(folder, path)) for path in video_inputs
])

# small_name = "my_concatenation_short.mp4"
# video_clip.resize(width=100).write_videofile(os.path.join(folder, small_name))
# video_clip = VideoFileClip(os.path.join(folder, small_name))
# save low quality version for preview and editing

fastest = 50 * 3
very_high = 20 * 3
lil_high = 10 * 3
tiny_bit_high = 3 * 3
normal_speed = 1 * 3


video_clip_modified = concatenate_videoclips(
    [
        video_clip.subclip(t_start=0, t_end=33).speedx(factor=very_high),
        video_clip.subclip(t_start=33, t_end=35).speedx(factor=normal_speed),
        video_clip.subclip(t_start=35, t_end=(1, 8)).speedx(factor=very_high),
        video_clip.subclip(t_start=(1, 8), t_end=(1, 11)).speedx(factor=tiny_bit_high),
        video_clip.subclip(t_start=(1, 8), t_end=(1, 11)).speedx(factor=tiny_bit_high).fx(vfx.time_mirror),
        video_clip.subclip(t_start=(1, 8), t_end=(1, 11)).speedx(factor=tiny_bit_high),
        video_clip.subclip(t_start=(1, 8), t_end=(1, 11)).speedx(factor=tiny_bit_high).fx(vfx.time_mirror),
        video_clip.subclip(t_start=(1, 8), t_end=(1, 11)).speedx(factor=tiny_bit_high),
        video_clip.subclip(t_start=(1, 8), t_end=(1, 11)).speedx(factor=tiny_bit_high).fx(vfx.time_mirror),

        video_clip.subclip(t_start=(1, 11), t_end=(1, 44)).speedx(factor=very_high),
        video_clip.subclip(t_start=(1, 44), t_end=(1, 55)).speedx(factor=lil_high),
        video_clip.subclip(t_start=(1, 55), t_end=(2, 36)).speedx(factor=tiny_bit_high),  # flour
        video_clip.subclip(t_start=(2, 36), t_end=(6, 13)).speedx(factor=lil_high),
        video_clip.subclip(t_start=(6, 13), t_end=(6, 16)).speedx(factor=normal_speed),  # camera fall
        video_clip.subclip(t_start=(6, 16), t_end=(6, 32)).speedx(factor=very_high),
        video_clip.subclip(t_start=(6, 32), t_end=(6, 34)).speedx(factor=normal_speed),  # camera fall 2
        video_clip.subclip(t_start=(6, 34), t_end=(7, 5)).speedx(factor=very_high),
        video_clip.subclip(t_start=(7, 5), t_end=(9, 5)).speedx(factor=lil_high),
        video_clip.subclip(t_start=(9, 5), t_end=(9, 10)).speedx(factor=normal_speed),  # butter
        video_clip.subclip(t_start=(9, 10), t_end=(9, 30)).speedx(factor=tiny_bit_high),
        video_clip.subclip(t_start=(9, 30), t_end=(9, 45)).speedx(factor=normal_speed),  # roll
        video_clip.subclip(t_start=(9, 45), t_end=(11, 30)).speedx(factor=lil_high),

        video_clip.subclip(t_start=(11, 30), t_end=(11, 50)).speedx(factor=normal_speed),  # roll

        video_clip.subclip(t_start=(11, 50), t_end=(12, 50)).speedx(factor=lil_high),
        video_clip.subclip(t_start=(12, 50), t_end=(12, 55)).speedx(factor=normal_speed),  # photo
        video_clip.subclip(t_start=(12, 55), t_end=(14, 5)).speedx(factor=lil_high),
        video_clip.subclip(t_start=(14, 5), t_end=(14, 10)).speedx(factor=normal_speed),  # paper on top

        video_clip.subclip(t_start=(14, 10), t_end=(15, 25)).speedx(factor=tiny_bit_high),
        video_clip.subclip(t_start=(15, 25), t_end=(15, 30)).speedx(factor=normal_speed),  # photo


        video_clip.subclip(t_start=(15, 30), t_end=(16, 11)).speedx(factor=tiny_bit_high),
        video_clip.subclip(t_start=(16, 11), t_end=(16, 24)).speedx(factor=normal_speed),  # fold

        video_clip.subclip(t_start=(16, 24), t_end=(16, 50)).speedx(factor=tiny_bit_high),
        video_clip.subclip(t_start=(16, 50), t_end=(17, 5)).speedx(factor=normal_speed),  # fridge


        video_clip.subclip(t_start=(17, 5), t_end=(18, 15)).speedx(factor=very_high),
        video_clip.subclip(t_start=(18, 15), t_end=(18, 50)).speedx(factor=lil_high),
        video_clip.subclip(t_start=(18, 50), t_end=(19, 10)).speedx(factor=normal_speed),  # flatten

        video_clip.subclip(t_start=(19, 10), t_end=(20, 30)).speedx(factor=lil_high),
        video_clip.subclip(t_start=(20, 30), t_end=(20, 35)).speedx(factor=normal_speed),  # flatten more

        video_clip.subclip(t_start=(20, 35), t_end=(21, 45)).speedx(factor=lil_high),

        video_clip.subclip(t_start=(21, 45), t_end=(22, 23)).speedx(factor=normal_speed),  # photo and fold

        video_clip.subclip(t_start=(22, 23), t_end=(22, 42)).speedx(factor=tiny_bit_high),
        video_clip.subclip(t_start=(22, 42), t_end=(22, 45)).speedx(factor=normal_speed),  # fridge

        video_clip.subclip(t_start=(22, 45), t_end=(23, 0)).speedx(factor=lil_high),  # end sequence
        video_clip.subclip(t_start=(23, 0), t_end=(25, 0)).speedx(factor=lil_high),
        video_clip.subclip(t_start=(25, 0), t_end=(25, 5)).speedx(factor=normal_speed),  # photo and sugar

        video_clip.subclip(t_start=(25, 5), t_end=(25, 45)).speedx(factor=tiny_bit_high),
        video_clip.subclip(t_start=(25, 5), t_end=(25, 45)).speedx(factor=lil_high).fx(vfx.time_mirror),
        video_clip.subclip(t_start=(25, 5), t_end=(25, 45)).speedx(factor=lil_high),
        video_clip.subclip(t_start=(25, 5), t_end=(25, 45)).speedx(factor=lil_high).fx(vfx.time_mirror),
        video_clip.subclip(t_start=(25, 5), t_end=(25, 45)).speedx(factor=lil_high),

        video_clip.subclip(t_start=(25, 45), t_end=(26, 50)).speedx(factor=tiny_bit_high),
        video_clip.subclip(t_start=(26, 50), t_end=(26, 55)).speedx(factor=normal_speed),  # fold sugar
        video_clip.subclip(t_start=(26, 55), t_end=(26, 17)).speedx(factor=tiny_bit_high),
        video_clip.subclip(t_start=(26, 17), t_end=(26, 19)).speedx(factor=normal_speed),  # fold sugar
        video_clip.subclip(t_start=(26, 19), t_end=(26, 30)).speedx(factor=tiny_bit_high),
        video_clip.subclip(t_start=(26, 30), t_end=(26, 32)).speedx(factor=normal_speed),  # fold sugar
        video_clip.subclip(t_start=(26, 32), t_end=(28, 20)).speedx(factor=tiny_bit_high),
        video_clip.subclip(t_start=(28, 20), t_end=(28, 22)).speedx(factor=normal_speed),  # fridge

        video_clip.subclip(t_start=(28, 22), t_end=(28, 52)).speedx(factor=lil_high),
        video_clip.subclip(t_start=(28, 52), t_end=(28, 57)).speedx(factor=normal_speed),  # un-fridge

        video_clip.subclip(t_start=(28, 57), t_end=(30, 30)).speedx(factor=tiny_bit_high),
        video_clip.subclip(t_start=(30, 30), t_end=(30, 50)).speedx(factor=normal_speed),

        video_clip.subclip(t_start=(30, 30), t_end=(30, 50)).speedx(factor=lil_high).fx(vfx.time_mirror),
        video_clip.subclip(t_start=(30, 30), t_end=(30, 50)).speedx(factor=lil_high),
        video_clip.subclip(t_start=(30, 30), t_end=(30, 50)).speedx(factor=lil_high).fx(vfx.time_mirror),
        video_clip.subclip(t_start=(30, 30), t_end=(30, 50)).speedx(factor=lil_high),

        video_clip.subclip(t_start=(30, 50), t_end=(31, 50)).speedx(factor=lil_high),
        video_clip.subclip(t_start=(31, 50), t_end=(32, 0)).speedx(factor=normal_speed),  # fold
        video_clip.subclip(t_start=(32, 0), t_end=(33, 0)).speedx(factor=lil_high),
        video_clip.subclip(t_start=(33, 0), t_end=(33, 5)).speedx(factor=normal_speed),

        video_clip.subclip(t_start=(33, 5), t_end=(33, 5)).speedx(factor=lil_high),
        video_clip.subclip(t_start=(33, 5), t_end=(33, 50)).speedx(factor=tiny_bit_high),
        video_clip.subclip(t_start=(33, 50), t_end=(33, 52)).speedx(factor=normal_speed),
        video_clip.subclip(t_start=(33, 52), t_end=(33, 57)).speedx(factor=tiny_bit_high),
        video_clip.subclip(t_start=(33, 57), t_end=(33, 59)).speedx(factor=normal_speed),

        video_clip.subclip(t_start=(33, 57), t_end=(33, 59)).speedx(factor=lil_high).fx(vfx.time_mirror),
        video_clip.subclip(t_start=(33, 57), t_end=(33, 59)).speedx(factor=lil_high),
        video_clip.subclip(t_start=(33, 57), t_end=(33, 59)).speedx(factor=lil_high).fx(vfx.time_mirror),
        video_clip.subclip(t_start=(33, 57), t_end=(33, 59)).speedx(factor=lil_high),

        video_clip.subclip(t_start=(33, 59), t_end=(39, 32)).speedx(factor=lil_high),
        video_clip.subclip(t_start=(39, 32), t_end=(39, 45)).speedx(factor=normal_speed),
        video_clip.subclip(t_start=(39, 45), t_end=(41, 5)).speedx(factor=lil_high),
        video_clip.subclip(t_start=(41, 5), t_end=(41, 15)).speedx(factor=normal_speed),
        video_clip.subclip(t_start=(41, 15), t_end=(42, 20)).speedx(factor=lil_high),
        video_clip.subclip(t_start=(42, 20), t_end=(42, 25)).speedx(factor=normal_speed),
        video_clip.subclip(t_start=(42, 25), t_end=(43, 8)).speedx(factor=lil_high),
        video_clip.subclip(t_start=(43, 8), t_end=(43, 15)).speedx(factor=normal_speed),
        video_clip.subclip(t_start=(43, 15), t_end=(44, 22)).speedx(factor=lil_high),
        video_clip.subclip(t_start=(44, 22), t_end=(44, 25)).speedx(factor=normal_speed),  # last roll
        video_clip.subclip(t_start=(44, 25), t_end=(45, 30)).speedx(factor=fastest),
        video_clip.subclip(t_start=(45, 30), t_end=(46, 20)).speedx(factor=very_high),
        video_clip.subclip(t_start=(46, 20)).speedx(factor=fastest),
    ]
).set_fps(60)
print(f"Original video clip duration:\t{video_clip.duration:10} "
      f"- {datetime.timedelta(seconds=video_clip.duration)}")
print(f"Modified video clip duration:\t{video_clip_modified.duration:10} "
      f"- {datetime.timedelta(seconds=video_clip_modified.duration)}")

picture = ImageClip(os.path.join(folder, "photo.jpg"))

video_clip_with_final = concatenate_videoclips(([
    video_clip_modified,
    # picture.set_duration(1).set_pos('center'),
]))\
    .add_mask()


w, h = video_clip_with_final.size
fps = video_clip_with_final.fps
duration = video_clip_with_final.duration
print(f"fps{video_clip_with_final.fps}")
print(f"Final Duration:\t{video_clip_with_final.duration}")


def final_blur(t):
    # print(f"Frame counting\t{t:.2f}\t{datetime.datetime.now().microsecond / 1e6:0.2f}"
    #       f"\t{datetime.datetime.now().second}")
    return circle(
        screensize=(w, h),
        center=(w/2, h/2),
        radius=max(0, (duration - t) / 20) * w,  # all seconds
        col1=1, col2=0.2, blur=4
    )


video_clip_with_final.mask.get_frame = final_blur


final_clip = CompositeVideoClip(
    [
        picture.set_duration(video_clip_with_final.duration).set_pos('center'),
        video_clip_with_final,
    ],
    size=video_clip_with_final.size)


final_clip = final_clip.set_audio(audioclip=audio_clip)

print(f"finalfps{final_clip.fps}")
print(f"finalduration{final_clip.duration}")

# final_clip.subclip(0).preview(fps=30, audio=False)

final_clip.write_videofile(os.path.join(folder, "my_concatenation_main.mp4"))
