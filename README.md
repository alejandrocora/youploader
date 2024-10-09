# Youploader - Automated YouTube Video Uploader and Reporter

`Youploader` is a command-line tool designed to automate YouTube video uploads and video reporting. It allows users to upload videos with custom metadata or report YouTube videos by specifying URLs, all from the convenience of a terminal. This program supports headless mode for background operation and allows you to log the output for later review.

## Features

- **Automated Video Upload**: Upload videos with metadata (title, description) directly to your YouTube account.
- **Video Reporting**: Report inappropriate or violating videos by providing their URLs.
- **Headless Mode**: Run the browser in headless mode for seamless background operations.
- **Log Output**: Optionally save the output log to a file for record-keeping or debugging.

## Installation

To use `Youploader`, clone the repository and install any required dependencies. Ensure Python is installed on your machine.

```bash
git clone https://github.com/your-repo/youploader.git
cd youploader
pip install -r requirements.txt
```

## Usage

`Youploader` can be used to either upload videos to YouTube or report videos. The options and commands are as follows:

```bash
youploader [-h] [--email EMAIL] [--password PASSWORD] [--upload] [--report] [--reason REASON] [--headless] [--output OUTPUT] targets [targets ...]
```

### Positional Arguments

- **targets**: Path(s) to the video(s) to upload or URL(s) to report.

  - For uploading videos, use the following format:
    ```json
    {"path":"/tmp/video.mp4", "title":"Example Title", "description":"Example description"}
    ```
  - For reporting videos, provide the URL(s) of the videos to be reported.

### Options

- `-h`, `--help`: Display help information and usage instructions.
- `--email EMAIL`: The email address for logging into the YouTube account.
- `--password PASSWORD`: The password for the YouTube account.
- `--upload`: Indicates that the program should upload the provided video(s).
- `--report`: Indicates that the program should report the provided video(s).
- `--reason REASON`: Specify the reason for reporting a video. Use the position number from a list of report reasons provided by YouTube.
- `--headless`: Run the browser in headless mode, which hides the graphical interface for background execution.
- `--output OUTPUT`: Specify a file to save the program's output log.

### Example Commands

#### Uploading a Video

```bash
youploader --email your-email@gmail.com --password your-password --upload '{"path":"/tmp/video.mp4", "title":"My Video Title", "description":"My Video Description"}'
```

#### Reporting a Video

```bash
youploader --email your-email@gmail.com --password your-password --report --reason 1 https://www.youtube.com/watch?v=example-url
```

#### Running in Headless Mode

```bash
youploader --email your-email@gmail.com --password your-password --upload --headless '{"path":"/tmp/video.mp4", "title":"My Video Title", "description":"My Video Description"}'
```

#### Saving the Output Log

```bash
youploader --email your-email@gmail.com --password your-password --upload --output log.txt '{"path":"/tmp/video.mp4", "title":"My Video Title", "description":"My Video Description"}'
```