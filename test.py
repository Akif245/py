# import sys
# sys.stdout.reconfigure(encoding='utf-8')
# import os

# video_url = "https://www.youtube.com/watch?v=yhGtJ6mFuwQ"
# output_dir = "C:/Users/Mohammed Abrar Ahmed/Desktop/PY"

# # Make sure the folder exists
# os.makedirs(output_dir, exist_ok=True)

# # Download using yt-dlp
# os.system(f'yt-dlp -o "{output_dir}/%(title)s.%(ext)s" {video_url}')

# print("Download complete!")

import sys
sys.stdout.reconfigure(encoding='utf-8')
import os

# Playlist URL instead of single video
playlist_url = "https://www.youtube.com/watch?v=FjHGZj2IjBk&list=RDQMrmN2lPAEVfc&start_radio=1"
output_dir = "C:/Users/Mohammed Abrar Ahmed/Desktop/PY"

# Make sure the folder exists
os.makedirs(output_dir, exist_ok=True)

# Download whole playlist
os.system(f'yt-dlp -o "{output_dir}/%(playlist_index)s - %(title)s.%(ext)s" {playlist_url}')

print(" Playlist download complete!")
