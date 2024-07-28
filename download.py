from pytube import YouTube
import os

# Get the YouTube video URL from the user
video_url = input("Enter the YouTube video URL: ")

# Create a YouTube object
yt = YouTube(video_url)

print(yt.title)
yt.streams

# # Get the highest resolution video stream
# stream = yt.streams.get_highest_resolution()

# # Set the download path to the current directory
# download_path = os.path.dirname(os.path.abspath(__file__))

# # Download the video
# stream.download(download_path)

# print("Video downloaded successfully!")


