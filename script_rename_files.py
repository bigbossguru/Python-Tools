from pathlib import Path
from tkinter import filedialog as fd

from utils import generate_random_string


def main():
    dir_path = Path(fd.askdirectory())

    for file in dir_path.rglob("*.*"):
        prefix = generate_random_string(5)
        new_file_path = file.parent.joinpath(f"{prefix}_{file.name}")
        file.rename(new_file_path)
        file.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
