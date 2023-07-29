import sys
import json

from tabulate import tabulate


def main():
    if len(sys.argv) != 2:
        print("Usage: python show_jupyter_codeblock.py <path/to/notebook.ipynb>")
        return

    path = sys.argv[1]
    data = json.load(open(path))

    sources = []
    for cell in data["cells"]:
        if cell["cell_type"] == "code":
            source = "".join(cell["source"])
            sources.append([source])

    print(tabulate(sources, tablefmt="grid", headers=["source"]))


if __name__ == "__main__":
    main()
