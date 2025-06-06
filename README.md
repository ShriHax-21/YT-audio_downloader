# ShriHax YouTube Downloader

A simple, terminal-based YouTube downloader written in Python using [yt-dlp](https://github.com/yt-dlp/yt-dlp).  
Supports audio (mp3) and video downloads, lets you choose resolution, works for playlists and single videos.

---

## Features

- **Download audio (mp3)** or **video** from YouTube URLs (single video or playlist)
- **Choose video resolution** (2160, 1440, 1080, 720, 480, 360, best...)
- **Automatic yt-dlp installation** (pip, apt, or brew)
- **No mouse or GUI needed**, just terminal and keyboard

---

## Requirements

- Python 3.x
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) (auto-installs if missing)
- `pip`, `apt`, or `brew` for auto-install (or install yt-dlp manually)

---

## Usage

1. **Save the script**

    Save the following as `yt_downloader.py`:

    ```python
    #!/usr/bin/env python3
    import os
    import subprocess
    import sys
    import shutil

    def print_logo():
        logo = r"""
      _____ _          _ _    _            
     / ____| |        (_) |  | |           
    | (___ | |__  _ __ _| |__| | __ ___  __
     \___ \| '_ \| '__| |  __  |/ _` \ \/ /
     ____) | | | | |  | | |  | | (_| |>  < 
    |_____/|_| |_|_|  |_|_|  |_|\__,_/_/\_\                
              ShriHax
        """
        print(logo)

    def check_yt_dlp():
        if shutil.which("yt-dlp"):
            return
        print("yt-dlp not found. Attempting to install...")
        if shutil.which("pip"):
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", "yt-dlp"])
                return
            except subprocess.CalledProcessError:
                print("Failed to install yt-dlp with pip.")
        if shutil.which("apt"):
            try:
                subprocess.check_call(["sudo", "apt", "update"])
                subprocess.check_call(["sudo", "apt", "install", "-y", "yt-dlp"])
                return
            except subprocess.CalledProcessError:
                print("Failed to install yt-dlp with apt.")
        if shutil.which("brew"):
            try:
                subprocess.check_call(["brew", "install", "yt-dlp"])
                return
            except subprocess.CalledProcessError:
                print("Failed to install yt-dlp with brew.")
        print("Please install yt-dlp manually from https://github.com/yt-dlp/yt-dlp")
        sys.exit(1)

    def download_audio(url: str, download_folder: str = "download") -> None:
        os.makedirs(download_folder,
