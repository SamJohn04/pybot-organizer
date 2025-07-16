import time
from pathlib import Path


def search_dir(dir_path: Path, dest_dirs: dict[str, Path]) -> None:
    """
    Search through a directory and move the files that match.
    """
    assert dir_path.is_dir(), f"{dir_path} is not a directory."

    for child_path in dir_path.iterdir():
       destination = find_item_in_dest(child_path, dest_dirs)
       if destination is not None:
            move_file(child_path, destination)


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


def find_item_in_dest(path: Path, dest_dirs: dict[str, Path]) -> Path | None:
    """
    Find file in destination diirectories.
    """
    # Update To Follow
    if path.suffix in dest_dirs:
        return dest_dirs[path.suffix]
    return None

