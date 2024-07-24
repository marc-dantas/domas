from argparse import ArgumentParser, Namespace
from collections import defaultdict
from enum import Enum, auto
from os import listdir
from os.path import exists, isdir, splitext
from os.path import join as pathjoin
from typing import Union
from sys import stderr
from PIL import Image

COLORS = {
    'white': (255, 255, 255, 255),
    'black': (0, 0, 0, 255),
    'red': (255, 0, 0, 255),
    'green': (0, 255, 0, 255),
    'blue': (0, 0, 255, 255),
    'purple': (255, 0, 255, 255),
    'yellow': (255, 255, 0, 255),
}


class Format(Enum):
    png = auto()
    jpeg = auto()
    bmp = auto()
    gif = auto()
    
    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return self.name

    @staticmethod
    def match_format(target: str) -> Union['Format', None]:
        if target == "png":
            return Format.png
        elif target in ("jpg", "jpeg"):
            return Format.jpeg
        elif target in ("bmp", "bitmap"):
            return Format.bmp
        elif target == "gif":
            return Format.gif
        else:
            return None


def parse_args() -> Namespace:
    p = ArgumentParser(
        "domas", description="dynamic binary visualization"
    )
    p.add_argument("path", help="file or directory to read file(s)")
    p.add_argument("-o", "--output", required=False,
                   help="output filename to write the final image")
    p.add_argument("-s", "--smooth", required=False, action="store_true",
                   help="apply smooth brightness adjustment based on pixel frequency")
    # TODO: Add scaling process to images to make it bigger
    # p.add_argument("-x", "--scale", required=False, default="1",
    #                help="apply scaling to the final image in times (default 1x 256x256)")
    p.add_argument("-f", "--format", required=False, default="png",
                   help="change format of the final image (default PNG)")
    p.add_argument("--background", required=False,
                   help="background color of the final image (default black)", default="black")
    p.add_argument("--foreground", required=False,
                   help="foreground color of the final image (default white)", default="white")
    return p.parse_args()


def smooth_color(c1: tuple, c2: tuple, factor: float, multiplier: int) -> tuple:
    return (
        int((c1[0] * factor + c2[0]) / 255 * multiplier),
        int((c1[1] * factor + c2[1]) / 255 * multiplier),
        int((c1[2] * factor + c2[2]) / 255 * multiplier),
        255
    )

def domas(path: str, o: Union[str, None], color: tuple, smooth: bool, f: Format) -> None:
    bg = COLORS['black'] if color[0] is None else color[0]
    fg = COLORS['white'] if color[1] is None else color[1]

    if not exists(path):
        print(f"domas: error: no such file {path}.", file=stderr)
        exit(1)
    
    image = Image.new(mode="RGB", size=(256, 256), color=bg)
    data = defaultdict(int)

    with open(path, "rb") as file:
        x = file.read()
        for coord in zip(x, x[1:]):
            data[coord] += 1

    for coord, fact in data.items():
        if not smooth:
            image.putpixel(coord, fg)
            continue
        image.putpixel(coord, smooth_color(fg, bg, fact, 10))
    
    print(f"domas: info: file {path} processed.", file=stderr)

    if o is None:
        output = f"{splitext(path)[0]}.out.{f}"

    with open(output, "wb") as out:
        image.save(out, format=str(f))

    print(f"domas: info: image {output} saved.", file=stderr)


def main() -> None:
    args = parse_args()

    if args.background not in COLORS:
        print(f"domas: error: invalid background {args.background}.", file=stderr)
        exit(1)

    if args.foreground not in COLORS:
        print(f"domas: error: invalid foreground {args.foreground}.", file=stderr)
        exit(1)

    bg = COLORS.get(args.background, None)
    fg = COLORS.get(args.foreground, None)
    f = Format.match_format(args.format)
    if f is None:
        print(f"domas: error: invalid file format specification {args.format}.", file=stderr)
        exit(1)
    
    if isdir(args.path):
        for p in listdir(args.path):
            p = pathjoin(args.path, p)
            if isdir(p):
                continue
            domas(p, args.output, (bg, fg), args.smooth, f)
        return

    domas(args.path, args.output, (bg, fg), args.smooth, f)


if __name__ == "__main__":
    main()
