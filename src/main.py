import time
from pathlib import Path

import constants


def main(dir_path: Path) -> None:
    """
    Search through a directory and move the files that match.
    """
    if not dir_path.is_dir():
        print("The given path is not a directory")
        return

    for child_path in dir_path.iterdir():
        if child_path.is_file() and child_path.suffix in constants.DEST_DIR:
            move_file(child_path, constants.DEST_DIR[child_path.suffix])


def move_file(src_path: Path, dest_dir: Path) -> None:
    """
    Moves a file. If a file with the same name exists, append timestamp.
    """
    # Create directory if it does not exist
    if not dest_dir.exists():
        dest_dir.mkdir(parents=True)

    # If not a directory
    if not dest_dir.is_dir():
        print(f"Destination {dest_dir} is not a directory.")
        return

    file_name = src_path.name
    dest_path = dest_dir / file_name

    # If name already exists
    if dest_path.exists():
        timestamp = int(time.time())
        dest_path = dest_dir / f"{dest_path.stem}_{timestamp}{dest_path.suffix}"

    # Move the file
    src_path.rename(dest_path)
    print(f"Moved: {src_path} -> {dest_path}")


if __name__ == '__main__':
    print(f"Searching through directory: {constants.SEARCH_DIR}")
    main(constants.SEARCH_DIR)

