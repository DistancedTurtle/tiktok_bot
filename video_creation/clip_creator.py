import moviepy.editor as mpy
import random
import os

def get_random_clip(audio_length, post_id):
    time_1 = random.randint(5, (480 - audio_length))
    clip1 = mpy.VideoFileClip('BackgroundGameplay.mp4').subclip(time_1, time_1+audio_length)
    clip1.write_videofile(f"{post_id}.mp4")

def compile_audio_video(post_id):
    audio = mpy.AudioFileClip(f'{post_id}.mp3')
    video = mpy.VideoFileClip(f'{post_id}.mp4')
    final_clip = video.set_audio(audio)
    final_clip.write_videofile(f'compiled_{post_id}')
    os.remove(f'{post_id}.mp3')
    os.remove(f'{post_id}.mp4')