# Edit THIS file to change the directories searched through and moved to.
from pathlib import Path


# The directory path searched through
SEARCH_DIR: Path = Path("/home/samuel-john/Downloads")

# The directory paths copied to
DEST_DIR: dict[str, Path] = {
        ".pdf": Path("/home/samuel-john/Documents/PDFs"),
        ".png": Path("/home/samuel-john/Pictures"),
        ".jpg": Path("/home/samuel-john/Pictures"),
        ".jpeg": Path("/home/samuel-john/Pictures"),
        ".webp": Path("/home/samuel-john/Pictures"),
        ".mp3": Path("/home/samuel-john/Music"),
        ".mp4": Path("/home/samuel-john/Music"),
        }

