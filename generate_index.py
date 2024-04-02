from pathlib import Path
from datetime import datetime

def format_relref_path(path, root_path):
    """Format a path as a Hugo relref shortcode."""
    rel_path = path.relative_to(root_path).as_posix()
    return f"{{{{< relref \"/{rel_path}\" >}}}}"

def generate_blog_links_and_folders(folder, root_path):
    """Generate markdown links for files and collapsed entries for directories."""
    entries = []
    for item in sorted(folder.iterdir()):
        if item.is_dir():
            # Check if the directory contains an _index.md to consider it for a collapsed entry
            if (item / "_index.md").exists():
                title = item.name.replace('_', ' ').title()
                entries.append(f"- [Collapsed]({format_relref_path(item, root_path)})")
        elif item.is_file() and item.suffix == ".md" and item.name != "_index.md":
            title = item.stem.replace('_', ' ').title()
            entries.append(f"- [{title}]({format_relref_path(item, root_path)})")
    return "\n".join(entries)

def generate_index_md(path: Path):
    """Generate _index.md files with links for MD files and collapsed entries for folders."""
    for folder in path.glob("**/*"):
        if folder.is_dir() and not folder.name.startswith('.'):
            index_file = folder / "_index.md"
            title = folder.name.replace("_", " ").title()
            date = datetime.now().strftime('%Y-%m-%d')
            content = f"---\ntitle: \"{title}\"\ndate: {date}\n---\n\n"
            entries_content = generate_blog_links_and_folders(folder, path)
            if entries_content:
                content += entries_content
            index_file.write_text(content)

# Specify the root directory for the content
content_path = Path("./content")

# Generate _index.md files
generate_index_md(content_path)
