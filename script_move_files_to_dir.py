import shutil
from pathlib import Path
from tkinter import filedialog as fd

from utils import generate_random_string


def main():
    dir_path = Path(fd.askdirectory())
    new_dir_path = dir_path / "final"
    new_dir_path.mkdir(exist_ok=True)

    for file in dir_path.rglob("*.*"):
        if file.suffix:
            shutil.move(file, new_dir_path / f"{generate_random_string(5)}_{file.name}")


if __name__ == "__main__":
    main()
