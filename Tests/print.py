from loadModules import load
load()
from DirItems.FolderManager import FolderManager

banned = set(['.venv', '__pycache__', '.git'])
folder_manager = FolderManager(r"D:\GitHub\Folderly", banned)
folder_manager.print()