import yt_dlp
import os
import sys

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def ask(prompt, valid=None):
    while True:
        value = input(prompt).strip()
        if not valid or value.lower() in valid:
            return value.lower()
        print("❌ Invalid choice. Try again.")

def download_media(url, mode, quality):
    if mode == "audio":
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": f"{DOWNLOAD_DIR}/%(title)s.%(ext)s",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": quality,
            }],
        }
    else:
        ydl_opts = {
            "format": quality,
            "outtmpl": f"{DOWNLOAD_DIR}/%(title)s.%(ext)s",
        }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\n✅ Download completed successfully!")
    except Exception as e:
        print("\n❌ Error occurred:")
        print(e)
        sys.exit(1)

def main():
    print("=" * 45)
    print(" YT Media Downloader | TINKLER MODE ")
    print("=" * 45)

    url = input("🔗 Enter YouTube URL: ").strip()
    if not url:
        print("❌ URL cannot be empty")
        return

    mode = ask(
        "🎧 Download audio or 🎥 video? (audio/video): ",
        valid=["audio", "video"]
    )

    if mode == "audio":
        quality = input("🎵 Audio quality (128 / 192 / 320) [192]: ").strip()
        quality = quality if quality else "192"
    else:
        quality = input(
            "🎞 Video quality (best / 720 / 480) [best]: "
        ).strip()

        if quality == "720":
            quality = "bestvideo[height<=720]+bestaudio"
        elif quality == "480":
            quality = "bestvideo[height<=480]+bestaudio"
        else:
            quality = "best"

    print("\n📥 Starting download...\n")
    download_media(url, mode, quality)

if __name__ == "__main__":
    main()
