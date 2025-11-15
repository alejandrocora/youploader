[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)]()
[![Python](https://img.shields.io/badge/python-3.13.7-blue.svg)](https://www.python.org/)
![Selenium](https://img.shields.io/badge/Selenium-4.32.0-blue.svg?logo=selenium&logoColor=white)
[![License: GPL v3](https://img.shields.io/badge/license-GPLv3-lightgray.svg)](LICENSE)
![Status](https://img.shields.io/badge/status-deprecated-red)
![Maintenance](https://img.shields.io/badge/maintenance-no_longer_maintained-red)


# ⚠️ Project Status: Deprecated & Unmaintained

> **IMPORTANT:**  
> Youploader is no longer maintained.  
> Google/YouTube updated their authentication systems, and the automated login method used by this tool **no longer works**.  
> The project remains public for archival and educational purposes only.

---

# Youploader  
### _Automated YouTube Video Uploader and Reporter_

`Youploader` is a command-line utility designed to automate YouTube video uploads and video reporting actions. It allows users to upload videos with custom metadata or report YouTube videos directly from the terminal. The tool supports headless mode for background operation and can optionally save logs for later review.

Although this project is no longer functional due to YouTube login changes, the documentation below reflects how it originally worked.

---

## ✨ Features

- **Automated Video Upload** – Upload videos with custom metadata (title, description).  
- **Video Reporting** – Report inappropriate content using video URLs.  
- **Headless Mode** – Run uploads/reports in the background without opening a browser window.  
- **Output Logging** – Optionally save the tool’s output to a file.

---

## 📦 Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/alejandrocora/youploader
cd youploader
pip install -r requirements.txt
```

---

## 🚀 Usage

`Youploader` can upload videos or report existing YouTube videos.

```
youploader [-h] [--email EMAIL] [--password PASSWORD] [--upload] [--report] 
           [--reason REASON] [--headless] [--output OUTPUT] targets [targets ...]
```

---

## 🔧 Positional Arguments

### **targets**
Path(s) to video(s) for upload **or** URL(s) of videos to report.

**Upload format:**
```json
{"path":"/tmp/video.mp4", "title":"Example Title", "description":"Example description"}
```

**Report format:**  
Use direct YouTube video URLs.

---

## 🛠️ Options

| Option | Description |
|--------|-------------|
| `-h`, `--help` | Show help information |
| `--email EMAIL` | YouTube account email |
| `--password PASSWORD` | YouTube account password |
| `--upload` | Upload provided videos |
| `--report` | Report provided videos |
| `--reason REASON` | Position number of YouTube’s report reason |
| `--headless` | Runs browser in headless mode |
| `--output OUTPUT` | Save program output to a file |

---

## 📘 Examples

### **Upload a Video**
```bash
youploader --email your-email@gmail.com --password your-password \
--upload '{"path":"/tmp/video.mp4", "title":"My Video Title", "description":"My Video Description"}'
```

### **Report a Video**
```bash
youploader --email your-email@gmail.com --password your-password \
--report --reason 1 https://www.youtube.com/watch?v=example-url
```

### **Headless Mode**
```bash
youploader --email your-email@gmail.com --password your-password \
--upload --headless '{"path":"/tmp/video.mp4", "title":"My Video Title", "description":"My Video Description"}'
```

### **Save Output Log**
```bash
youploader --email your-email@gmail.com --password your-password \
--upload --output log.txt '{"path":"/tmp/video.mp4", "title":"My Video Title", "description":"My Video Description"}'
```

---

## ⚠️ Final Note

This project is kept online for reference only.  
The YouTube login flow used by `Youploader` has been patched and automated login is no longer possible without major rework and new authentication handling.