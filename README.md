# 🎵 YouTube Playlist Audio Downloader

A Python script to download **audio from a YouTube playlist** and convert it to **MP3 format** using `yt-dlp` and `ffmpeg`.

---

## 🛠 Requirements

* Python 3.7+
* [`yt-dlp`](https://github.com/yt-dlp/yt-dlp)
* [`ffmpeg`](https://ffmpeg.org/)

---

## 📦 Installation

### 1. Clone the Repository (Optional)

```bash
git clone https://github.com/ShriHax-21/yt-audio_downloader.git
cd yt-audio_downloader
```

### 2. Create Virtual Environment
"pip" doesn`t work on shell so we have to create venv enviroments 
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

---

If you want me to add or tweak anything, just say!
