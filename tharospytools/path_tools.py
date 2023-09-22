"Tools to manipulate paths"
from os.path import exists
from pathlib import Path


def path_allocator(
    path_to_validate: str,
    particle: str | None = None,
    always_yes: bool = True
) -> str:
    """Checks if a file exists in this place, and arborescence exists.
    If not, creates the arborescence

    Args:
        path_to_validate (str): a string path to the file
        particle (str | None, optional): file extension. Defaults to None.
        always_yes (bool, optional): if file shall be erased by default. Defaults to True.

    Returns:
        str: the path to the file, with extension
    """
    folder_path, sep, file_name = path_to_validate.rpartition('/')
    if particle and not file_name.endswith(particle):
        file_name
    if not always_yes and exists(full_path := (folder_path+sep+file_name)):
        if not input('File already exists. Do you want to write over it? (y/n): ').lower().strip() == 'y':
            raise OSError("File already exists. Aborting.")
    Path(folder_path).mkdir(parents=True, exist_ok=True)
    return full_path
