# Domas
Domas is a very simple console application I built to implement the Dynamic Binary Visualization algorithm described by Christopher Domas.

> Reference: [4 2 1 Christopher Domas The future of RE Dynamic Binary Visualization](https://www.youtube.com/watch?v=4bM3Gut1hIk&t=0s) and [Christopher Domas aka the delta axiom The Future of RE Dynamic Binary Visualization](https://www.youtube.com/watch?v=sUSFGXFo-Pw)

## Getting Started

### Setup
Domas is written in Python, so you need the latest version of the Python interpreter installed on your machine.

To install all the dependencies of the application, you can just use `pip`.

Inside the repository's directory, run:
```console
$ pip install -r requirements.txt
```
Now you're ready to use Domas!

### Usage

To use Domas, just run the main script file at the `src` directory:
```console
$ python3 src/domas.py
```

If you do not provide any file, the help message will show and from that you can start messing around...

You can also customize the final generated image using the `--foreground` and `--background` flags, these are all the possible colors:

- White: `white`
- Black: `black`
- Red: `red`
- Green: `green`
- Blue: `blue`
- Purple: `purple`
- Yellow: `yellow`

### Examples
There's a directory which has some files to play around with. You can generate the images for each file inside the folder by running:

```console
$ python src/domas.py ./examples
```

---

> By Marcio Dantas
