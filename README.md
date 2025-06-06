---

# 🎥 ShriHax YouTube Downloader

A terminal-based YouTube **audio & video downloader** built with Python and [`yt-dlp`](https://github.com/yt-dlp/yt-dlp).
Supports downloading **MP3 audio** or **high-resolution videos** from **individual videos or playlists**.
Automatically installs `yt-dlp` if not already present.

---

## 🛠 Requirements

* Python 3.7+
* [`yt-dlp`](https://github.com/yt-dlp/yt-dlp)
* [`ffmpeg`](https://ffmpeg.org/) (only for audio conversion)
* Terminal / Command-line

---

## ⭐ Features

* 🎵 **Download audio (MP3)** or 🎞️ **video** from YouTube
* 📺 Supports both **single videos** and **playlists**
* 📽️ Choose custom resolution (e.g., 1080p, 720p, or "best")
* 🚀 Auto-installs `yt-dlp` using `pip`, `apt`, or `brew`
* 🧰 Lightweight CLI with **no GUI required**
* 📂 Save files with readable, clean filenames

---

## 📦 Installation

### 1. Clone the Repository (Optional)

```bash
git clone https://github.com/ShriHax-21/YouTube-Downloader.git
cd YouTube-Downloader
```

### 2. Create Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install Dependencies

```bash
pip install yt-dlp
```

### 4. Install ffmpeg (required for audio download)

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

You will be prompted to:

* Select between **audio** or **video** download
* Enter the **YouTube URL** (video or playlist)
* Optionally provide a **download folder**
* For video: choose the **desired resolution**

---

## 📂 Output

* Downloads and saves all selected content
* Audio is converted to **MP3** using `ffmpeg`
* Files are stored in the chosen folder with descriptive names

---

## 🧪 Example

```bash
🎵 YouTube Downloader

Choose download type:
1. Audio only (MP3, works for playlist or single video)
2. Video (works for playlist or single video)
Enter 1 for Audio or 2 for Video: 1
Enter YouTube video or playlist URL: https://www.youtube.com/playlist?list=PLabc...
Enter download folder (default: download): 
```

---

## 🐞 Troubleshooting

### 🔴 ERROR: `yt-dlp not found`

The script auto-installs `yt-dlp`, but if all methods fail:

* Install manually using:

```bash
pip install yt-dlp
```

Or follow instructions on [yt-dlp GitHub](https://github.com/yt-dlp/yt-dlp)

---

### 🔴 ERROR: `ffmpeg not found`

Make sure `ffmpeg` is installed and accessible:

```bash
ffmpeg -version
```

If the command fails, [install ffmpeg](https://ffmpeg.org/download.html) and ensure it’s added to your system PATH.

---

## 📃 License

MIT License.
Free to use, share, and modify.

---