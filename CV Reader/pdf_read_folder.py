from pathlib import Path
import os
from os import listdir
from os.path import isfile, join

Files_Path = (Path.cwd())
Files_Path = str(Files_Path) + "\\CVs"
Files_Path = Path(Files_Path)

print(Files_Path)

def obtain_cv(i):
    onlyfiles = [f for f in listdir(Files_Path) if isfile(join(Files_Path, f))]
    cv_path = Path(str(Files_Path) + "\\" +  onlyfiles[i])
    return cv_path