#!/usr/bin/env python3
import os
import argparse
from jinja2 import Environment, FileSystemLoader

def main():
    parser = argparse.ArgumentParser(description="dp-gen: Design Pattern Code Scaffolder")
    subparsers = parser.add_subparsers(dest="command")

    # 'make' command
    make_parser = subparsers.add_parser("make", help="Generate boilerplate for a design pattern")
    make_parser.add_argument("pattern", help="Design pattern name (e.g., strategy, factory)")
    make_parser.add_argument("name", nargs="?", default=None, help="Custom name for the pattern classes")
    make_parser.add_argument("--lang", default="csharp", help="Target language (default: csharp)")
    make_parser.add_argument("--out", default=".", help="Output directory (default: current directory)")

    args = parser.parse_args()

    if args.command == "make":
        generate_pattern(args.pattern, args.name, args.lang, args.out)
    else:
        parser.print_help()

def generate_pattern(pattern, custom_name, lang, out_dir):
    # Templates are now inside the package
    template_dir = os.path.join(os.path.dirname(__file__), "templates", lang, pattern)
    
    if not os.path.exists(template_dir):
        print(f"Error: Pattern '{pattern}' for language '{lang}' not found in {template_dir}")
        return

    # Default name if not provided
    if not custom_name:
        custom_name = pattern.capitalize()

    env = Environment(loader=FileSystemLoader(template_dir))
    
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    print(f"Generating {pattern} pattern in {lang}...")

    for template_name in env.list_templates():
        if not template_name.endswith(".j2"):
            continue
            
        template = env.get_template(template_name)
        
        # Determine output filename: remove .j2 and replace 'Pattern' with custom_name
        output_name = template_name.replace(".j2", "")
        # Replace occurrences of capitalized pattern name if it exists in filename
        # e.g., IStrategy.cs -> IMyStrategy.cs
        placeholder = pattern.capitalize()
        if placeholder in output_name:
            output_name = output_name.replace(placeholder, custom_name)
        else:
            # Fallback: prefix the filename if it doesn't contain the pattern name
            # This is a simple heuristic
            pass

        output_path = os.path.join(out_dir, output_name)
        
        content = template.render(
            name=custom_name,
            pattern=pattern,
            lang=lang
        )
        
        with open(output_path, "w") as f:
            f.write(content)
        
        print(f"  Created {output_path}")

if __name__ == "__main__":
    main()
