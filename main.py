from DirItems.FolderManager import FolderManager

banned = set(['.venv', '__pycache__', '.git'])
folder_manager = FolderManager(r"C:\Users\48519558\Desktop", banned)
folder_manager.print()