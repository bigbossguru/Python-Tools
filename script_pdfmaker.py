import argparse
from pathlib import Path
from tkinter import filedialog as fd

from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()


def pdf_maker(args: argparse.Namespace) -> None:
    dir_path = get_dir_path(args.input_dir)
    filenames = get_filepaths(dir_path, args.input_file_extension)

    try:
        filenames = sorted(
            filenames,
            key=lambda path: int(path.stem.split('_')[0]),
        )
    except ValueError:
        pass

    if len(filenames) <= 0:
        print(f"No {args.input_file_extension} files found")
        return None

    images = [Image.open(f) for f in filenames]
    images_resize = resize_images(images, args.resize_ratio, args.alignment)

    pdf_filepath = dir_path / f"{args.output_pdfname}.pdf"
    images_resize[0].save(
        pdf_filepath,
        save_all=True,
        append_images=images_resize[1:],
        optimize=args.optimize,
        quality=args.quality,
    )
    print(f"Finished successfully: {pdf_filepath}")


def get_filepaths(dir_path: Path, file_extension: list[str]) -> list[Path]:
    filepaths = []
    for ext in file_extension:
        filepaths += list(dir_path.glob(f"*.{ext.lower()}"))
    return filepaths


def get_dir_path(dir_path: str | None) -> Path:
    if not dir_path:
        return Path(fd.askdirectory())
    return Path(dir_path)


def resize_images(
    images: list[Image.Image],
    resize_ratio: float = 1.0,
    alignment: bool = False,
) -> list[Image.Image]:
    resized_images = []

    if alignment:
        max_size_alignment = max([img.size for img in images])

    for img in images:
        if alignment and img.size < max_size_alignment:
            width, height = max_size_alignment
        else:
            width, height = img.size

        new_size = (int(width // resize_ratio), int(height // resize_ratio))
        resized_images.append(img.resize(new_size))
    return resized_images


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input-dir", required=False)
    parser.add_argument("-o", "--output-pdfname", default="lekarska_zprava", type=str)
    parser.add_argument(
        "-ext", "--input-file-extension", nargs="+", default=["HEIC", "JPG"], type=str
    )
    parser.add_argument("-sr", "--resize-ratio", default=1.5, type=float)
    parser.add_argument("-q", "--quality", default=80, type=int)
    parser.add_argument("-opt", "--optimize", action="store_false")
    parser.add_argument("-a", "--alignment", action="store_true")
    args = parser.parse_args()
    print(args)
    pdf_maker(args)
