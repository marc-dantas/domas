# Domas
Domas is a very simple console application I built to implement a Dynamic Binary Visualization algorithm. This algorithm was described by Christopher Domas (that's why it's called Domas), and its purpose is to detect file types by making a very simple file analysis.

> "_If we change the way we process binary information... we find unexpected ways of making sense of it_".

## How it works

> **DISCLAIMER**: I'm not Christopher Domas, so maybe all this explanation is just wrong. I'm just saying what **I** understood about the idea.

RE Dynamic Binary Visualization is an Reverse Engineering algorithm originally made to identify patterns in sequences of bytes by iterating over all the pairs of bytes and drawing a point on an image, threating the byte pair like (x, y) coordinates.

This can seem a bit nonsense but it actually generates really interesting patterns depending on the sequence of bytes. Here are some examples (you can see all these files in the `examples` folder):



| **Text** | **Image** | **Executable** | **Audio** |
| --- | --- | --- | --- |
| ![Text](./examples/output/lorem.out.png)  | ![Image](./examples/output/bliss.out.png) | ![Executable](./examples/output/program.out.png) | ![Audio](./examples/output/starwars.out.png) |


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
