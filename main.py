import glob
import os
from subprocess import call

from config import parse_opts

config = parse_opts()
def generate_segments(input_video, dest_dir):
    cmd = 'ffmpeg -re -i '+ input_video +' -map 0 -map 0 -c:a aac -c:v libx264 -b:v:0 800k -b:v:1 300k -s:v:1 320x170 -profile:v:1 baseline -profile:v:0 main -bf 1 -keyint_min 120 -g 120 -sc_threshold 0 -b_strategy 0 -ar:a:1 22050 -use_timeline 1 -use_template 1 -window_size 5 -adaptation_sets "id=0,streams=v id=1,streams=a" -f dash ' +dest_dir+'out.mpd'

    print(cmd)
    call(cmd,shell=True)

def vid2wav(input_video, dest_dir):
    cmd = 'ffmpeg -i ' + input_video +' -ac 2 -f wav ' + dest_dir + '/input.wav'
    print(cmd)
    call(cmd,shell=True)

def wav2mp3(input_dir, dest_dir):
    cmd = 'ffmpeg -i '+input_dir+'/input.wav -vn -ar 44100 -ac 2 -b:a 192k '+ dest_dir+'/input.mp3'     
    print(cmd)
    call(cmd,shell=True)

def vid2frames(input_video, dest_dir):
    cmd = 'ffmpeg -i ' + input_video +' -qscale:v 2 -vf fps=1 ' + dest_dir + '/02%d.jpg'
    print(cmd)
    call(cmd,shell=True)

def start_process(input_path, output_path):
    for file_name in [input_path]:
        video_list = glob.glob(file_name + '*.mp4')
        for video in video_list:
            print('-'*60)
            print('File Name: ', video)

            video_file_name = video.split('\\')[-1].split(".")[0]

            main_video_path = os.path.join(output_path, video_file_name)
            seg_path = os.path.join(main_video_path, 'segments')
            audio_path = os.path.join(main_video_path, 'audio')
            frames_path = os.path.join(main_video_path, 'frames')
            thumbnail_path = os.path.join(main_video_path, 'thumbnails')
            
            # Split the video into HLS segments
            if not os.path.exists(seg_path):
                print(seg_path)
                os.makedirs(seg_path)
                generate_segments(video, seg_path + '/')
            
            # Extract audio
            if config.audio:
                if not os.path.exists(audio_path):
                    print(audio_path)
                    os.makedirs(audio_path)    
                    vid2wav(video, audio_path)
                    #comment if you don't want to convert to mp3
                    wav2mp3(audio_path, audio_path)

            # Extract frames
            if config.frames:
                if not os.path.exists(frames_path):
                    print(frames_path)
                    os.makedirs(frames_path)
                    vid2frames(video, frames_path)

  
if __name__ == '__main__':
    start_process(config.inp_path, config.out_path)
    print('All process completed')
    
    
