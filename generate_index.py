from pathlib import Path

def generate_index_md(path: Path):
    """
    Generates _index.md files for each directory and subdirectory within the given path.
    The _index.md file will have the folder name as the title.
    """
    for folder in path.rglob("*"):
        if folder.is_dir():
            index_file = folder / "_index.md"
            title = folder.name.replace("_", " ").title()
            content = f"---\ntitle: \"{title}\"\ndescription: \"\"\n---\n\n"
            blogs = []

            for item in folder.iterdir():
                if item.is_file() and item.suffix == ".md" and item.name != "_index.md":
                    blogs.append(item.stem.replace("_", " ").title())
                elif item.is_dir():
                    sub_index = item / "_index.md"
                    if sub_index.exists():
                        blogs.append(f"[{item.name.replace('_', ' ').title()}]({{< relref \"{item.relative_to(path)}\" >}})")

            if blogs:
                content += "## Blogs\n" + "\n".join(f"- {blog}" for blog in blogs)

            with index_file.open("w") as file:
                file.write(content)

def generate_menu(path: Path, menu_file: Path):
    """
    Generates a markdown file for the menu based on the directory structure starting from the given path.
    """
    def create_menu_entry(path: Path, level=0):
        menu = ""
        indent = "  " * level
        if path.is_dir():
            title = path.name.replace("_", " ").title()
            if path.name != "posts":
                menu += f'{indent}- **{title}**\n'
            for item in sorted(path.iterdir()):
                if item.is_dir() or (item.is_file() and item.suffix == ".md" and item.name != "_index.md"):
                    menu += create_menu_entry(item, level + 1)
        elif path.is_file() and path.suffix == ".md" and path.name != "_index.md":
            title = path.stem.replace("_", " ").title()
            menu += f'{indent}- [{title}]({{< relref "/{path.relative_to(path.parents[2])}" >}})\n'
        return menu

    menu_content = create_menu_entry(path)
    with menu_file.open("w") as file:
        file.write(menu_content)

# Specify the root directory for the content and the menu output file path
posts_path = Path("./content/posts")
docs_path = Path("./content/docs")
menu_path = Path("./content/menu/index.md")

# Generate _index.md files and the menu
generate_index_md(posts_path)
generate_index_md(docs_path)
generate_menu(posts_path, menu_path)
