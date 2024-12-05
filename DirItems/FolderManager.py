from pathlib import Path
import sys
sys.path.append(Path(__file__).parent)
from .file import File
from .folder import Folder
from rich.console import Console
from rich.table import Table 

class FolderManager:
    def __init__(self, root: str, banned: set[str]) -> None:
        self.root: Path = Path(root)
        self.rootFolder: Folder = Folder(self.root, banned, parent=None)
        self.children: list[File | Folder] = self.rootFolder.children
        self.console = Console()

    def print(self) -> None:
        self.console.print(f"[bold green]Folder:[/bold green] {self.root}")
        self._print_folder_table(self.rootFolder)

    def _print_folder_table(self, folder: Folder) -> None:
        table = Table(title=f"[blue]{folder.path}[/blue]")
        table.add_column("Path", justify="left")
        table.add_column("Name", justify="left")
        table.add_column("Type", justify="center")
        table.add_column("Extension", justify="center")
        table.add_column("Size", justify="right")
        table.add_column("Last Modified", justify="right")

        for child in self.children:
            table.add_row(
                str(child.path),
                child.name,
                "Folder" if isinstance(child, Folder) else "File",
                child.type if isinstance(child, File) else "None",
                f"{child.size} bytes" if isinstance(child, File) else "None",
                child.lastModified if isinstance(child, File) else "None",
                style="bold green" if isinstance(child, File) else "bold blue"
            )
        self.console.print(table)
        for child in self.children:
            if isinstance(child, Folder):
                child.print_table(self.console)

    def makeDiagram(self) -> None:
        pass

    def saveDiagram(self) -> None:
        pass

