from DirItems.FolderManager import FolderManager

banned = set(['.venv', '__pycache__', '.git'])
folder_manager = FolderManager(r"C:\Users\matia\OneDrive\Escritorio\Folderly", banned)
folder_manager.print()