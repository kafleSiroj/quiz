from moviepy.editor import VideoFileClip

def play():
    video_path = 'modules/media/video.mp4'
    video = VideoFileClip(video_path)
    video.preview()
