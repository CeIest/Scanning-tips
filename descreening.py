
from tkinter.filedialog import askdirectory
from tkinter import Tk
import subprocess
import pathlib
import click
import sys
import os

#https://github.com/6o6o/fft-descreen


if len(sys.argv) > 1:
    src_folder = str(sys.argv[1]).replace("\\", "/")
else:
    Tk().withdraw()
    src_folder = askdirectory()
    print(src_folder)


print("====================")

for root, _, files in os.walk(src_folder):
    for file_name in files:
        with open(os.path.join(root, file_name), 'br+') as f:
            if file_name.endswith(".jpg"):
                
                filename_export = pathlib.Path(file_name).stem
                
                os.makedirs(f"{src_folder}/Descreen", exist_ok=True)
            
                print(f"Descreening {filename_export}...")
                commandlossless = f'descreen.py "{src_folder}/{file_name}" "{src_folder}/Descreen/{filename_export}.jpg"'
                subprocess.run(commandlossless, shell=True, check=True)

print("====================")

click.secho("\nDescreen complete.", fg="green")
