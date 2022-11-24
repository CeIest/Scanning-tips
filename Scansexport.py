import os
import subprocess
import pathlib 

for root, _, files in os.walk('.'):
    for file_name in files:
        with open(os.path.join(root, file_name), 'br+') as f:
            if file_name.endswith(".psd"):
                
                filename_export = pathlib.Path(file_name).stem
                
                
                commandlossless = 'i_view64.exe "' + file_name + '" /pngc=9 /fullinfo /transpcolor=(r,g,b) /convert="Export/' + filename_export + '.png"'
                print("LOSSLESS export of " + filename_export)
                subprocess.call(commandlossless)

                commandlossy = 'i_view64.exe "' + file_name + '" /resize=(0,2048) /aspectratio /fullinfo /resample /jpgq=100 /dpi=(72,72) /convert="Export/WEB/' + filename_export + '.jpg"'
                print("WEB export of " + filename_export)
                subprocess.call(commandlossy)


print("\nEXPORT complete.")

