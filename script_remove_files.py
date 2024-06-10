from pathlib import Path
from tkinter import filedialog as fd


def main():
    dir_path = Path(fd.askdirectory())

    # !!!! Set up file ext 
    for file in dir_path.rglob("*.aae"):
        file.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
