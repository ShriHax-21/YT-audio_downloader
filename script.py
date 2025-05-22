import os
import subprocess

def download_playlist_with_ytdlp(playlist_url, download_folder="downloads"):
    os.makedirs(download_folder, exist_ok=True)
    
    # Construct yt-dlp command
    command = [
        "yt-dlp",
        "-f", "bestaudio",
        "--extract-audio",
        "--audio-format", "mp3",
        "--output", f"{download_folder}/%(title)s.%(ext)s",
        playlist_url
    ]

    try:
        subprocess.run(command, check=True)
        print("\n✅ All downloads complete.")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ yt-dlp failed: {e}")

if __name__ == "__main__":
    playlist_url = input("Enter YouTube playlist URL: ").strip()
    download_folder = input("Enter download folder (default: downloads): ").strip() or "downloads"
    download_playlist_with_ytdlp(playlist_url, download_folder)
