from googleapiclient.discovery import build
from pytube import YouTube
from moviepy.video.io.VideoFileClip import VideoFileClip

api_key = 'YOUR YOUTUBE API KEY'
youtube = build('youtube', 'v3', developerKey=api_key)
channel_id = 'CHANNEL ID YOU WANT TO DOWNLOAD FROM'  

def get_videos(channel_id):
    request = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        maxResults=50,
        order="date"
    )
    response = request.execute()

    videos = []
    for item in response['items']:
        if item['id']['kind'] == 'youtube#video':
            videos.append(item['id']['videoId'])
    return videos

def download_video(video_id):
    url = f'https://www.youtube.com/watch?v={video_id}'
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True,file_extension='mp4').first()
    stream.download(filename=f'{video_id}.mp4')

def split_video(video_id):
    video = VideoFileClip(f'{video_id}.mp4')
    video_duration = video.duration
    clip_duration = 30  # Duration of each clip in seconds
    clip_count = int(video_duration // clip_duration)
    
    for i in range(clip_count + 1):
        start_time = i * clip_duration
        end_time = start_time + clip_duration
        if end_time > video_duration:
            end_time = video_duration

        clip = video.subclip(start_time, end_time)
        clip_filename = f'{video_id}_clip_{i+1}.mp4'
        clip.write_videofile(clip_filename, codec='libx264')

    video.close()

# Main script
video_ids = get_videos(channel_id)

for video_id in video_ids:
    download_video(video_id)
    split_video(video_id)
