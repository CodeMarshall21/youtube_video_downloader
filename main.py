from pytube import Playlist

def download_videos(playlist_url, download_path="."):
    # Create a Playlist object
    playlist = Playlist(playlist_url)
    
    print(f'Downloading playlist: {playlist.title}')
    print(f'Total videos: {len(playlist.video_urls)}')
    
    # Loop through all videos in the playlist and download them
    for video in playlist.videos:
        print(f'Downloading: {video.title}')
        video.streams.get_highest_resolution().download(output_path=download_path)
        print(f'Completed: {video.title}')
    
    print('All videos have been downloaded.')

if __name__ == "__main__":
    playlist_url = input("Enter the YouTube playlist URL: ")
    download_path = input("Enter the download path (leave empty for current directory): ") or "."
    download_videos(playlist_url, download_path)
#hi da this is an useless commit !
