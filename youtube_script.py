from pytube import YouTube


link = "https://www.youtube.com/watch?v=9PgtyeugRvU"
link = "https://www.youtube.com/watch?v=9HGh8f7Twn8"
output_folder = "output"


yt = YouTube(link)
# stream = yt.streams.all()
# for s in stream:
#     print(s)
#     s.download(output_path=output_folder, filename=f"{s}")


# yt.streams\
#     .filter(progressive=True, file_extension='mp4')\
#     .order_by('resolution')\
#     .first()\
#     .download(output_path=output_folder, filename_prefix="progressive")
#
# yt.streams\
#     .filter(progressive=False, file_extension='webm')\
#     .order_by('resolution')\
#     .last()\
#     .download(output_path=output_folder, filename_prefix="video")

out = yt.streams\
    .filter(progressive=False, file_extension='webm')\
    .order_by('abr')\
    .last()\
    .download(output_path=output_folder, filename_prefix="audio")
print(out)
