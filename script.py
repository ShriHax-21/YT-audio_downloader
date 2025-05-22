import os
import subprocess
import sys

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


def download_playlist_audio(playlist_url: str, download_folder: str = "downloads") -> None:
    """
    Downloads audio from a YouTube playlist using yt-dlp and converts to MP3.

    Args:
        playlist_url (str): The URL of the YouTube playlist.
        download_folder (str): Path to save downloaded audio files.
    """
    os.makedirs(download_folder, exist_ok=True)

    command = [
        "yt-dlp",
        "-f", "bestaudio",
        "--extract-audio",
        "--audio-format", "mp3",
        "--output", os.path.join(download_folder, "%(title)s.%(ext)s"),
        playlist_url
    ]

    print(f"\nStarting download to folder: '{download_folder}'\n")
    try:
        subprocess.run(command, check=True)
        print("\n✅ All downloads completed successfully.")
    except subprocess.CalledProcessError as err:
        print(f"\n❌ yt-dlp failed with error:\n{err}")
        sys.exit(1)


def main():
    print_logo()

    print("🎵 YouTube Playlist Audio Downloader\n")

    playlist_url = input("Enter YouTube playlist URL: ").strip()
    if not playlist_url:
        print("Error: Playlist URL cannot be empty.")
        sys.exit(1)

    download_folder = input("Enter download folder (default: downloads): ").strip() or "downloads"

    download_playlist_audio(playlist_url, download_folder)


if __name__ == "__main__":
    main()
