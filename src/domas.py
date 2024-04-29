from argparse import ArgumentParser, Namespace
from os import listdir
from os.path import exists, isdir, splitext
from os.path import join as pathjoin
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


def parse_args() -> Namespace:
    p = ArgumentParser(
        "domas", description="dynamic binary visualization"
    )
    p.add_argument("path", help="file or directory to read file(s)")
    p.add_argument("-o", "--output", required=False,
                   help="output filename to write the final image")
    p.add_argument("--background", required=False,
                   help="background color of the final image (default black)", default="black")
    p.add_argument("--foreground", required=False,
                   help="foreground color of the final image (default white)", default="white")
    return p.parse_args()


def domas(path: str, output: str, bg: tuple = None, fg: tuple = None) -> None:
    bg = COLORS['black'] if bg is None else bg
    fg = COLORS['white'] if fg is None else fg

    image = Image.new(mode="RGB", size=(256, 256), color=bg)

    if not exists(path):
        print(f"domas: error: no such file {path}.", file=stderr)
        exit(1)

    with open(path, "rb") as file:
        x = file.read()
        for coord in zip(x, x[1:]):
            image.putpixel(coord, fg)
    print(f"domas: info: file {path} processed.", file=stderr)

    if output is None:
        output = f"{splitext(path)[0]}.out.png"

    with open(output, "wb") as out:
        image.save(out)

    print(f"domas: info: image {output} saved.", file=stderr)


def main() -> None:
    args = parse_args()

    if args.background not in COLORS:
        print(f"domas: error: invalid background {args.background}.", file=stderr)
        exit(1)

    if args.foreground not in COLORS:
        print(f"domas: error: invalid foreground {args.background}.", file=stderr)
        exit(1)

    if isdir(args.path):
        for p in listdir(args.path):
            p = pathjoin(args.path, p)
            if isdir(p):
                continue
            domas(p, args.output, COLORS[args.background], COLORS[args.foreground])
        return

    domas(args.path, args.output, COLORS[args.background], COLORS[args.foreground])


if __name__ == "__main__":
    main()
