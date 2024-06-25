import tkinter as tk
from tkinter import filedialog, messagebox
from pytube import Playlist
from pytube import YouTube
import threading

class YouTubePlaylistDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Playlist Downloader")
        
        self.playlist_url_label = tk.Label(root, text="YouTube Playlist URL:")
        self.playlist_url_label.grid(row=0, column=0, padx=10, pady=10)
        
        self.playlist_url_entry = tk.Entry(root, width=50)
        self.playlist_url_entry.grid(row=0, column=1, padx=10, pady=10)

        self.video_url_label = tk.Label(root, text="YouTube URL:")
        self.video_url_label.grid(row=1, column=0, padx=10, pady=10)

        self.video_url_entry = tk.Entry(root, width=50)
        self.video_url_entry.grid(row=1, column=1, padx=10, pady=10)
        
        self.download_path_label = tk.Label(root, text="Download Path:")
        self.download_path_label.grid(row=2, column=0, padx=10, pady=10)
        
        self.download_path_entry = tk.Entry(root, width=50)
        self.download_path_entry.grid(row=2, column=1, padx=10, pady=10)
        
        self.browse_button = tk.Button(root, text="Browse", command=self.browse)
        self.browse_button.grid(row=2, column=2, padx=10, pady=10)
        
        self.download_button = tk.Button(root, text="Download", command=self.download_playlist)
        self.download_button.grid(row=3, column=1, padx=10, pady=10)
        
        
        
        self.status_label = tk.Label(root, text="", fg="blue")
        self.status_label.grid(row=4, column=0, columnspan=3, padx=10, pady=10)
    
    def browse(self):
        download_path = filedialog.askdirectory()
        if download_path:
            self.download_path_entry.delete(0, tk.END)
            self.download_path_entry.insert(0, download_path)


    def download_playlist(self):
        playlist_url = self.playlist_url_entry.get()
        download_path = self.download_path_entry.get()
        video_url = self.video_url_entry.get()


        if (video_url or playlist_url) and download_path:
            if video_url and not playlist_url:
                # self.status_label.config(text="Downloading...")
                threading.Thread(target=self.video_only, args=(video_url,download_path)).start()
                return
            
            if not video_url and playlist_url:
                # self.status_label.config(text="Downloading...")
                threading.Thread(target=self.download_videos, args=(playlist_url, download_path)).start()
                return
            
        else:
            messagebox.showerror("Error", "Please enter download path.")
            return
        
        
    def video_only(self,video_url,download_path):
        try:
            video = YouTube(video_url)
            self.status_label.config(text=f"Downloading: {video.title}")
            video.streams.get_highest_resolution().download(output_path=download_path) 
            self.status_label.config(text="Download completed.")
            messagebox.showinfo("Success", "video have been downloaded.")
            
            
        except Exception as e:
            self.status_label.config(text="")
            messagebox.showerror("Error", f"An error occurred: {e}")
    
    
    def download_videos(self, playlist_url, download_path):
        try:
            playlist = Playlist(playlist_url)
            total_videos = len(playlist.video_urls)
            
            for i, video in enumerate(playlist.videos):
                self.status_label.config(text=f"Downloading: {video.title} ({i+1}/{total_videos})")
                video.streams.get_highest_resolution().download(output_path=download_path)
            
            self.status_label.config(text="Download completed.")
            messagebox.showinfo("Success", "All videos have been downloaded.")
        except Exception as e:
            self.status_label.config(text="")
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubePlaylistDownloader(root)
    root.mainloop()
