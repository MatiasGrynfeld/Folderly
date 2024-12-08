from pathlib import Path
from .file import File
from typing import Union
from rich.table import Table
from rich.console import Console

class Folder:
    def __init__(self, path: Path, banned: set[str], parent: Union['Folder', None] = None) -> None:
        self.path: Path = path
        self.name: str = path.name
        self.parent: Folder | None = parent
        self.banned: set[str] = banned
        self.children: list[File | Folder] = []
        self.loadContent()

    def loadContent(self) -> None:
        for item in self.path.iterdir():
            if item.name not in self.banned:
                if item.is_file():
                    self.children.append(File(item))
                elif item.is_dir():
                    subfolder = Folder(item, banned=self.banned, parent=self)
                    self.children.append(subfolder)

    def print_table(self, console: Console) -> None:
        table = Table(title=f"[blue]{self.path}[/blue]")
        table.add_column("Path", justify="left")
        table.add_column("Name", justify="left")
        table.add_column("Type", justify="center")
        table.add_column("Extension", justify="center")
        table.add_column("Size", justify="right")
        table.add_column("Last Modified", justify="right")
        table.add_column("Last Opened", justify="right")
        for child in self.children:
            table.add_row(
                str(child.path),
                child.name,
                "Folder" if isinstance(child, Folder) else "File",
                child.type if isinstance(child, File) else " ",
                f"{child.size} bytes" if isinstance(child, File) else " ",
                child.lastModified if isinstance(child, File) else " ",
                child.access if isinstance(child, File) else " ",
                style="bold green" if isinstance(child, File) else "bold blue"
            )
        console.print(table)
        for child in self.children:
            if isinstance(child, Folder):
                child.print_table(console)