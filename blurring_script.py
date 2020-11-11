from moviepy.editor import vfx, VideoFileClip, TextClip, concatenate_videoclips
from moviepy.video.tools.tracking import manual_tracking
from moviepy.video.tools.tracking import Trajectory


# LOAD THE CLIP (subclip 6'51 - 7'01 of a chaplin movie)
clip = VideoFileClip("MoreGoproBike/GOPR5761.MP4").subclip((6, 51.7), (7, 01.3))

# MANUAL TRACKING OF THE HEAD

# the three next lines are for the manual tracking and its saving
# to a file, it must be commented once the tracking has been done
# (after the first run of the script for instance).
# Note that we save the list (ti,xi,yi), not the functions fx and fy
# (that we will need) because they have dependencies.


# trajectories = manual_tracking(clip, t1=5, t2=7, fps=5, nobjects=3, savefile="track.txt")


# IF THE MANUAL TRACKING HAS BEEN PREVIOUSLY DONE,
# LOAD THE TRACKING DATA AND CONVERT IT TO FUNCTIONS x(t),fy(t)

# traj,  =  Trajectory.load_list('track.txt')
traj1, traj2, traj3 = Trajectory.load_list('track.txt')

# BLUR CHAPLIN'S HEAD IN THE CLIP

# clip_blurred = clip.fx(vfx.headblur, traj1.xi, traj1.yi, 25)
# clip_blurred = vfx.headblur(clip=clip, traj=traj1, r_zone=25)
clip_blurred = clip.fx(vfx.headblur, traj1, 75)
clip_blurred = clip_blurred.fx(vfx.headblur, traj2, 75)
clip_blurred = clip_blurred.fx(vfx.headblur, traj3, 75)


# clip_blurred.write_videofile('blurredChaplin.mp4')

txt = TextClip("Hey you ! \n You're blurry!", color='grey70',
               size=clip.size, bg_color='grey20',
               font="Century-Schoolbook-Italic", fontsize=40)
final = concatenate_videoclips([clip_blurred, txt.set_duration(3)]). \
    set_audio(clip_blurred.audio)
final.write_videofile('blurredChaplin2.mp4')
