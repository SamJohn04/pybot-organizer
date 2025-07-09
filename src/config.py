import json


def read_config() -> tuple[str, dict[str, str]]:
    with open("config.json", "r") as fp:
        config = json.load(fp)

    return config["directory_to_search"], config["destination_directories"]


def write_config(user_config: tuple[str, dict[str, str]]) -> None:
    dir_to_search, dest_dirs = user_config
    
    config = {
            "directory_to_search": dir_to_search,
            "destination_directories": dest_dirs
            }

    with open("config.json", "w") as fp:
        json.dump(config, fp, indent=4)

