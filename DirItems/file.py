from pathlib import Path
from time import ctime
from rich.table import Table

class File:
    def __init__(self, path: Path) -> None:
        self.path: Path = path
        self.name: str = path.name
        self.size: int = self.getSize()
        self.lastModified: str = self.getLastModification()
        self.type: str = self.getType()

    def getSize(self) -> int:
        return self.path.stat().st_size

    def getLastModification(self) -> float:
        return ctime(self.path.stat().st_mtime)

    def getType(self) -> str:
        return self.path.suffix

