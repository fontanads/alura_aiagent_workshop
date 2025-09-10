import os
import yaml


def read_yaml(path):
    with open(path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def write_env_from_dict(env_vars: dict, overwrite: bool = True) -> None:
    for key, value in env_vars.items():
        if overwrite or key not in os.environ:
            os.environ[key] = str(value)


def update_env_secrets(path_to_secrets: str):
    secrets = read_yaml(path_to_secrets)
    write_env_from_dict(secrets)