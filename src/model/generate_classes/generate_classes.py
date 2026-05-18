#!/usr/bin/env python3
"""Generate .hpp/.cpp stubs for OS: IDD object types and register them in CMakeLists.txt."""

import argparse
import re
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

SCRIPT_DIR = Path(__file__).parent
MODEL_DIR = SCRIPT_DIR.parent
IDD_FACTORY_CXX = MODEL_DIR.parent / "generateiddfactory" / "IddFactory.cxx"
CMAKE_FILE = MODEL_DIR / "CMakeLists.txt"
CMAKE_START = "# Start Additions from the python script"
CMAKE_END = "# End Additions from the python script"

GENERATED_DIR = MODEL_DIR / "generated"
GENERATED_DIR.mkdir(exist_ok=True)


def idd_to_class_name(idd_object_type: str) -> str:
    return idd_object_type.replace("OS:", "").replace(":", "").replace("-", "")

def parse_idd_object_types_from_factory() -> list[str]:
    text = IDD_FACTORY_CXX.read_text()

    # Isolate the const evalue a[] = { ... }; block
    array_match = re.search(r"const evalue a\[\] = \{(.+?)\};", text, re.DOTALL)
    if not array_match:
        raise ValueError(f"Could not find 'const evalue a[]' in {IDD_FACTORY_CXX}")

    # Each entry: {IddObjectType::Foo, "Foo", "Human:Readable:Name"},
    # Third quoted field is the IDD object type string.
    return re.findall(r'\{[^}]+,\s*"[^"]+",\s*"(OS:[^"]+)"\s*\}', array_match.group(1))


def render_templates(idd_object_type: str) -> None:
    env = Environment(loader=FileSystemLoader(SCRIPT_DIR), keep_trailing_newline=True)
    for ext in ("hpp", "cpp"):
        template = env.get_template(f"template.{ext}.j2")
        output = template.render(idd_object_type=idd_object_type)
        class_name = idd_to_class_name(idd_object_type=idd_object_type)
        (GENERATED_DIR / f"{class_name}.{ext}").write_text(output)
        print(f"  wrote {class_name}.{ext}")


def update_cmake(idd_object_types: list[str]) -> None:
    text = CMAKE_FILE.read_text()

    rel_dir = GENERATED_DIR.relative_to(MODEL_DIR)
    entries = []
    for idd_object_type in idd_object_types:
        class_name = idd_to_class_name(idd_object_type=idd_object_type)
        entries.append(f"  {rel_dir}/{class_name}.hpp")
        entries.append(f"  {rel_dir}/{class_name}.cpp")

    block = f"{CMAKE_START}\n" + "\n".join(entries) + f"\n  {CMAKE_END}"

    updated = re.sub(
        rf"{re.escape(CMAKE_START)}.*?{re.escape(CMAKE_END)}",
        block,
        text,
        flags=re.DOTALL,
    )

    CMAKE_FILE.write_text(updated)
    print(f"Updated {CMAKE_FILE.name}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-n", "--num-objects",
        type=int,
        default=10,
        metavar="N",
        help="Number of OS: types to generate from IddFactory.cxx (default: 10, -1 for all)",
    )
    args = parser.parse_args()

    all_types = parse_idd_object_types_from_factory()
    # Remove DefaultScheduleSet which we already added
    all_types = [t for t in all_types if t != "OS:DefaultScheduleSet"]
    idd_object_types = all_types if args.num_objects == -1 else all_types[:args.num_objects]
    print(f"Generating {len(idd_object_types)} of {len(all_types)} OS: types found in IddFactory.cxx")

    for idd in idd_object_types:
        print(f"  {idd}")
        render_templates(idd)

    update_cmake(idd_object_types)
