import sys
import os
from pathlib import Path
def load():
    sys.path.append(str(Path(os.getcwd()).parent))
    print(str(Path(os.getcwd()).parent))