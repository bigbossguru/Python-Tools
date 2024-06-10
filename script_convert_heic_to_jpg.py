from pathlib import Path
from tkinter import filedialog as fd

from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()


def main():
    dir_path = Path(fd.askdirectory())

    images = {f: Image.open(f) for f in dir_path.rglob("*.heic")}

    for file, img in images.items():
        try:
            img_path = file.parent.joinpath(file.stem + ".JPG")
            if not img_path.exists():
                img.save(
                    fp=img_path,
                    optimize=True,
                    quality=80,
                )
                file.unlink(missing_ok=True)
        except:
            pass


if __name__ == "__main__":
    main()
