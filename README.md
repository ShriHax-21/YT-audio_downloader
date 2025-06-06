# 🎵 YouTube Playlist Audio Downloader
# ShriHax YouTube Downloader
Add commentMore actions
A Python script to download **audio from a YouTube playlist** and convert it to **MP3 format** using `yt-dlp` and `ffmpeg`.
A simple, terminal-based YouTube downloader written in Python using [yt-dlp](https://github.com/yt-dlp/yt-dlp).  
Supports audio (mp3) and video downloads, lets you choose resolution, works for playlists and single videos.

---

## 🛠 Requirements
## Features

* Python 3.7+
* [`yt-dlp`](https://github.com/yt-dlp/yt-dlp)
* [`ffmpeg`](https://ffmpeg.org/)
- **Download audio (mp3)** or **video** from YouTube URLs (single video or playlist)
- **Choose video resolution** (2160, 1440, 1080, 720, 480, 360, best...)
- **Automatic yt-dlp installation** (pip, apt, or brew)
- **No mouse or GUI needed**, just terminal and keyboard

---

## 📦 Installation
## Requirements

### 1. Clone the Repository (Optional)

```bash
git clone https://github.com/yourname/yt-playlist-audio-downloader.git
cd yt-playlist-audio-downloader
```

### 2. Create Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install ffmpeg (if not already installed)

#### On Debian/Kali/Ubuntu:

```bash
sudo apt update
sudo apt install ffmpeg
```

#### On Windows:

Download and extract from [FFmpeg.org](https://ffmpeg.org/download.html), and add the `bin/` folder to your system PATH.

---

## ▶️ Usage

Run the script:

```bash
python3 script.py
```

You'll be prompted to enter:

* The YouTube **playlist URL**
* An optional download folder (default: `downloads/`)

---

## 📂 Output

* Downloads all audio tracks from the playlist.
* Converts them to **high-quality MP3** format.
* Saves them in the chosen folder with proper filenames.

---

## 🧪 Example

```bash
Enter YouTube playlist URL: https://www.youtube.com/playlist?list=PLxyz...
Enter download folder (default: downloads): 
```

---

## 🐞 Troubleshooting

### 🔴 ERROR: `ffmpeg not found`

Make sure `ffmpeg` is installed and accessible in your system PATH:

```bash
ffmpeg -version
```

If not, [install it here](https://ffmpeg.org/download.html).

---

## 📃 License

MIT License. Free to use and modify.
- Python 3.x
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) (auto-installs if missing)
- `pip`, `apt`, or `brew` for auto-install (or install yt-dlp manually)