import os
import subprocess
import pathlib 
#https://github.com/6o6o/fft-descreen


for root, _, files in os.walk('.'):
    for file_name in files:
        with open(os.path.join(root, file_name), 'br+') as f:
            if file_name.endswith(".jpg"):
                
                filename_export = pathlib.Path(file_name).stem
                
                os.makedirs("Descreen", exist_ok=True)
                commandlossless = 'descreen.py "' + file_name + '" "Descreen/' + filename_export + '.jpg"'
                print("Descreening " + filename_export + "...")
                subprocess.run(commandlossless, shell=True, check=True)

print("\nDescreen complete.")
