# dp-gen: Design Pattern Code Scaffolder

A simple CLI tool to generate boilerplate code for GoF Design Patterns.

## Installation

### Local Usage
1. Clone this repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Global Usage (Recommended)
To run `dp-gen` from anywhere:
1. Navigate to the project directory.
2. Install in editable mode (add `--break-system-packages` if on Linux and not in a venv):
   ```bash
   pip install -e . --break-system-packages
   ```
Now you can just type `dp-gen` in any terminal!

## Usage

Generate a design pattern boilerplate:

```bash
dp-gen make strategy --lang csharp
```

Generate a pattern with a custom name:

```bash
dp-gen make strategy Payment --lang csharp
```

Output directory:

```bash
python3 dp_gen.py make factory MyFactory --lang csharp --out ./output
```

## Supported Patterns

- `strategy` (C#, Python)
- `factory` (C#)
- `observer` (C#)
- `singleton` (C#)
- `decorator` (C#)

## Adding More Templates

Add your Jinja2 templates to `templates/<language>/<pattern>/`. Use `{{ name }}` for the custom name provided by the user.
