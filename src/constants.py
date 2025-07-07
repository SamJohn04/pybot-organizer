import json
from pathlib import Path


with open("config.json", "r") as fp:
    config = json.load(fp)

SEARCH_DIR: Path = Path(config["directory_to_search"])

DEST_DIR: dict[str, Path] = {
        extension: Path(destination)
        for extension, destination in config["destination_directories"].items()
        }

