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
|_____/|_| |_|_|_|  |_|  |_|\__,_/_/\_\                
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
    os.makedirs(download_folder, exist_ok=True)
    command = [
        "yt-dlp",
        "-f", "bestaudio",
        "--extract-audio",
        "--audio-format", "mp3",
        "--output", os.path.join(download_folder, "%(title)s.%(ext)s"),
        url
    ]
    print(f"\nStarting audio download to folder: '{download_folder}'\n")
    try:
        subprocess.run(command, check=True)
        print("\n✅ All audio download completed successfully.")
    except subprocess.CalledProcessError as err:
        print(f"\n❌ yt-dlp failed with error:\n{err}")
        sys.exit(1)

def download_video(url: str, download_folder: str = "download", resolution: str = "best") -> None:
    os.makedirs(download_folder, exist_ok=True)
    # Always use user-provided resolution, do not default to "best"
    format_selector = f"bestvideo[height={resolution}]+bestaudio/best[height={resolution}]/best"
    command = [
        "yt-dlp",
        "-f", format_selector,
        "-P", download_folder,
        url
    ]
    print(f"\nStarting video download to folder: '{download_folder}' with resolution: {resolution}\n")
    try:
        subprocess.run(command, check=True)
        print("\n✅ Video download completed successfully.")
    except subprocess.CalledProcessError as err:
        print(f"\n❌ yt-dlp failed with error:\n{err}")
        sys.exit(1)

def main():
    print_logo()
    print("🎵 YouTube Downloader\n")
    check_yt_dlp()

    print("Choose download type:")
    print("1. Audio only (MP3, works for playlist or single video)")
    print("2. Video (works for playlist or single video)")
    option = input("Enter 1 for Audio or 2 for Video: ").strip()

    url = input("Enter YouTube video or playlist URL: ").strip()
    if not url:
        print("Error: URL cannot be empty.")
        sys.exit(1)
    download_folder = input("Enter download folder (default: download): ").strip() or "download"

    if option == "1":
        download_audio(url, download_folder)
    elif option == "2":
        print("\nAvailable resolutions: 2160, 1440, 1080, 720, 480, 360")
        resolution = ""
        while not (resolution.isdigit() and int(resolution) > 0):
            resolution = input("Enter desired resolution (e.g., 1080 for 1080p): ").strip()
            if not (resolution.isdigit() and int(resolution) > 0):
                print("Please enter a valid numeric resolution (e.g., 1080).")
        download_video(url, download_folder, resolution)
    else:
        print("Invalid option selected. Exiting.")
        sys.exit(1)

if __name__ == "__main__":
    main()