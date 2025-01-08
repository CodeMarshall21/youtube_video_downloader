# ideas for gui.py
---
1. resolution options
2. time stamp
3. pause, stop download
4. mp3 extractor
5. range of video in playlist
6. hit `download` multiple times
7. message box for exception (paal kudi da)
8. Delpoy !

self.status_label = tk.Label(root, text="", fg="blue")
        self.status_label.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

        self.download_button = tk.Button(root, text="Download Video", command=self.download_playlist)
        self.download_button.grid(row=3, column=1, padx=10, pady=10)
