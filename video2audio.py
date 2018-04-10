import sys
import argparse
import moviepy.editor as movie_editor

parser = argparse.ArgumentParser(description='Convert video clip to audio file.')
parser.add_argument('video_path', metavar='video_path', type=str, help='Absolute path to video')
parser.add_argument('audio_name', metavar='audio_name', type=str, help='Audio name')
parser.add_argument('min', metavar='min', type=int, help='min value of sub-audio')
parser.add_argument('max', metavar='max', type=int, help='max vulue of sub-audio')
args = parser.parse_args()
print(args)

app_name, clip_path, output_name, min_time, max_time = sys.argv

clip = movie_editor.VideoFileClip(clip_path)

if min_time and max_time:
    if int(min_time) >= int(max_time):
        raise ValueError('max time must greater than min time')
    if int(min_time) < 0: min_time = 0
    if int(max_time) > clip.duration: max_time = duration
else:
    min_time, max_time = (0, clip.duration)

subclip = clip.subclip(int(min_time), int(max_time))

clip.audio.write_audiofile(output_name)

