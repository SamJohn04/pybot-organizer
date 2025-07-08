import json
from pathlib import Path


def read_config() -> tuple[Path, dict[str, Path]]:
    with open("config.json", "r") as fp:
        config = json.load(fp)

    dir_to_search: Path = Path(config["directory_to_search"])
    dest_dirs: dict[str, Path] = {
            extension: Path(destination)
            for extension, destination in config["destination_directories"].items()
            }

    return dir_to_search, dest_dirs

