"""
# Entry validated: output is 1-200 chars, one line, deterministic.
Entrypoint script for the grader. Writes a specific verbatim line to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os
import pathlib

LINE = "A midnight firmware update remapped my cotton filters as edible upholstery, and frankly, that argyle started it.\n"


def main() -> None:
    # Determine output directory
    out_dir_path = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    directory = pathlib.Path(out_dir_path)
    directory.mkdir(parents=True, exist_ok=True)

    output_file = directory / "entry.txt"

    # Validate content according to rules
    content = LINE
    if not (1 <= len(content) <= 200 and content.strip()):
        raise ValueError("Content validation failed")

    # Write UTF-8 file
    output_file.write_text(content, encoding="utf-8")

    # Print output path and character count
    print(output_file)
    print(len(content))


if __name__ == "__main__":
    main()
