import argparse
from pathlib import Path

from organizer import core, config


def main():
    args = parse_args()

    if args.action == 'WRITE':
        write()
    elif args.temp == None:
        search_and_move()
    else:
        search_and_move(args.temp)


def parse_args():
    parser = argparse.ArgumentParser(prog="organizer")
    parser.add_argument('-w', '--write',
                        help='write configuration.json',
                        action='store_const',
                        const='WRITE',
                        dest='action',
                        default='SEARCH')
    parser.add_argument('--temp',
                        help='temporarily use the following as the directory to search',
                        default=None)
    args = parser.parse_args()

    if args.action == 'WRITE' and args.temp is not None:
        print("--temp and --write flags are not allowed together. Ignoring the --temp flag.")

    return args


def search_and_move(searchable_dir: str | None = None):
    if searchable_dir is None:
        dir_to_search, dest_dirs = config.read_config()
    else:
        dir_to_search = searchable_dir
        _, dest_dirs = config.read_config()

    print(f"Searching through directory: {dir_to_search}")

    dir_to_search = Path(dir_to_search)
    dest_dirs = {
            end_of_name: Path(destination)
            for end_of_name, destination in dest_dirs.items()
            }

    try:
        core.search_dir(dir_to_search, dest_dirs)
    except AssertionError as e:
        print(e)
    except Exception as e:
        print("Something went wrong:", e)


def write():
    dest_dirs = {}
    dir_to_search = Path(input("Enter directory to perform searches at: ")).resolve()

    print("Looping, enter nothing to exit")

    end_of_name = input("End of file name (including extension): ")
    while end_of_name != "":
        dest_dirs[end_of_name] = Path(input("Destination: ")).resolve()

        end_of_name = input("End of file name (including extension): ")

    print("Directory To Search:", dir_to_search)
    print("Destination Directories: ", dest_dirs)

    if input("Do you wish to update your configuration? (y|N): ") != 'y':
        return

    dir_to_search = str(dir_to_search)
    dest_dirs = {
            end_of_name: str(destination)
            for end_of_name, destination in dest_dirs.items()
            }

    config.write_config((dir_to_search, dest_dirs))
    print("Configuration written.")


if __name__ == '__main__':
    main()

