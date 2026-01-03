# YT Media Downloader (CLI · Local-First · TINKLER Mode)

A **local-first command-line YouTube media downloader** designed for learning, understanding core concepts, and long-term offline use.

This project intentionally avoids online hosting and GUIs.
The goal is **control, clarity, and core understanding**, not convenience shortcuts.

AI was used as a development assistant, while all logic, flow, and behavior are fully understood and modifiable.

---

## 📌 Project Philosophy

> Tools already exist.
> What matters now is understanding how to use, modify, debug, and extend them.

This project demonstrates:
- Practical Python usage
- CLI tool design
- Integration with real-world utilities
- Ethical, local-first software thinking
- AI-assisted development with human control

---

## ✨ Features

- 📥 Download YouTube **audio (MP3)** or **video (MP4)**
- 🧩 Interactive **TINKLER mode** (guided prompts)
- 🖥 Runs directly from CMD / Terminal
- 📴 Fully offline after initial setup
- ♻ Works indefinitely (no server dependency)
- 🔧 Simple codebase, easy to extend

---

## ❌ Non-Goals (Important)

This project is intentionally **NOT**:
- An online downloader website
- A hosted service or API
- A browser-based tool
- A copyright bypass system
- Dependent on GitHub Pages runtime

---

## ⚖ Ethical Usage Notice

This tool is intended only for:
- Content you personally uploaded
- Content you have explicit permission to download
- Royalty-free or educational material

The author does not encourage misuse.
Users are responsible for how they use this tool.

---

## 🧰 Tech Stack

- **Python 3**
- **yt-dlp** – media extraction engine
- **FFmpeg** – audio/video processing
- **Command Line Interface (CLI)**

---

## 📁 Project Structure

```
yt-media-downloader-cli/
│
├── yt_downloader.py      # Main CLI script (TINKLER mode)
├── requirements.txt      # Python dependencies
└── downloads/            # Output directory
```

---

## ⚙ System Requirements

- Python **3.8+**
- FFmpeg installed and added to PATH
- Internet connection only during download

---

## 🛠 Installation

### 1️⃣ Install Python
Verify Python installation:
```bash
python --version
```

---

### 2️⃣ Install FFmpeg
FFmpeg is required for audio conversion.

Verify:
```bash
ffmpeg -version
```

If not installed, download FFmpeg and add it to your system PATH.

---

### 3️⃣ Install Python Dependencies
```bash
pip install -r requirements.txt
```

---

## ▶ Usage (TINKLER Mode)

Run the script:
```bash
python yt_downloader.py
```

The program will guide you interactively:
1. Enter YouTube URL
2. Choose audio or video
3. Select quality

No flags.
No memorization.
Just guided execution.

---

## 📂 Output

All downloaded files are saved to:
```
downloads/
```

Filenames are automatically generated using the video title.

---

## 🧠 How It Works (Core Understanding)

### yt-dlp
- Extracts metadata and media streams from YouTube
- Handles adaptive formats, playlists, and retries
- Acts as the primary extraction engine

### FFmpeg
- Converts audio streams into MP3
- Merges audio + video streams when needed
- Handles codec compatibility

### Python Script Role
- Collects user input (TINKLER mode)
- Builds yt-dlp configuration dynamically
- Manages download flow
- Handles errors and file output

The script is a **controller**, not a black box.

---

## 🧪 Design Decisions Explained

### Why CLI instead of GUI?
- CLI tools are faster, scriptable, and professional
- No UI framework dependency
- Easier to debug and extend
- Common in real-world engineering environments

### Why Local-First?
- No hosting cost
- No platform restrictions
- Works years later without changes
- Better learning experience

### Why Interactive (TINKLER) Mode?
- Reduces cognitive load
- Encourages experimentation
- Ideal for beginners and daily use
- Easier to understand than complex flags

---

## 🧠 Learning Outcomes

By building and using this project, you learn:
- CLI application design
- External tool integration
- Error handling in real systems
- How yt-dlp and FFmpeg interact
- How to use AI productively without dependency
- How to document and explain software clearly

---

## 🚀 Possible Extensions

- Playlist download support
- Download history logging
- Retry and network error classification
- Merge interactive + flag-based modes
- Package as a pip-installable tool
- Cross-platform installer scripts

---

## 👤 Author

**Anshu Goel**
Computer Teacher · Programmer · Freelancer

Focused on:
- Practical learning
- Automation
- CLI tooling
- AI-assisted development with core understanding

---

## 📜 License

This project is open-source and intended for educational purposes.

---
