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


def write_config(user_config: tuple[Path, dict[str, Path]]) -> None:
    dir_to_search, dest_dirs = user_config
    
    dir_to_search = str(dir_to_search.resolve())
    dest_dirs = {
            extension: str(destination.resolve())
            for extension, destination in dest_dirs.items()
            }
    
    config = {
            "directory_to_search": dir_to_search,
            "destination_directories": dest_dirs
            }

    with open("config.json", "w") as fp:
        json.dump(config, fp, indent=4)

