import time
import argparse
from pathlib import Path

from src import config


def main():
    args = parse_args()

    if args.write:
        write()
    else:
        search_and_move()


def parse_args():
    parser = argparse.ArgumentParser(prog="organizer")
    parser.add_argument('-w', '--write', help='write configuration.json', action='store_true')
    return parser.parse_args()


def search_and_move():
    dir_to_search, dest_dirs = config.read_config()
    print(f"Searching through directory: {dir_to_search}")

    dir_to_search = Path(dir_to_search)
    dest_dirs = {
            extension: Path(destination)
            for extension, destination in dest_dirs.items()
            }

    try:
        search_dir(dir_to_search, dest_dirs)
    except AssertionError as e:
        print(e)
    except Exception as e:
        print("Something went wrong:", e)


def write():
    dest_dirs = {}
    dir_to_search = Path(input("Enter directory to perform searches at: ")).resolve()

    print("Looping, enter nothing to exit")
    while True:
        extension = input("Extension (with full stop): ")
        if extension == "":
            break
        dest_dirs[extension] = Path(input("Destination: ")).resolve()

    print(dir_to_search)
    print(dest_dirs)

    if input("Do you wish to update your configuration? (y|N): ") != 'y':
        return

    dir_to_search = str(dir_to_search)
    dest_dirs = {
            extension: str(destination)
            for extension, destination in dest_dirs.items()
            }

    config.write_config((dir_to_search, dest_dirs))


def search_dir(dir_path: Path, dest_dirs: dict[str, Path]) -> None:
    """
    Search through a directory and move the files that match.
    """
    assert dir_path.is_dir(), f"{dir_path} is not a directory."

    for child_path in dir_path.iterdir():
        if child_path.is_file() and child_path.suffix in dest_dirs:
            move_file(child_path, dest_dirs[child_path.suffix])


def move_file(src_path: Path, dest_dir: Path) -> None:
    """
    Moves a file. If a file with the same name exists, append timestamp.
    """
    # Create directory if it does not exist
    if not dest_dir.exists():
        dest_dir.mkdir(parents=True)

    # Throw an error if not a directory
    assert dest_dir.is_dir(), f"{dest_dir} is not a directory."

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
    main()

