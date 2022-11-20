# Scanning-tips
## SCANNING

Scan at the highest DPI you can, output with a lossless format (TIFF, PNG...).<br>
Make sure to crop your debinded pages within your scanner's software if it's supported, according to your page's original aspect ratio.<br>
Else, batch crop with IrfanView.<br>
If the colours of the output seem off, you may auto-balance the brightness and saturation, but NOT the leveling.<br>
You may want to use the filters however you want, as long as it's not too much. (note: filters can be applied within photoshop during the editing process, so we can get clean files).<br>
![SCANNING 01](/Assets/Scanning-01.jpg)<br>
![SCANNING 02](/Assets/Scanning-02.jpg)<br>




## EDITING
If the scanned images are flipped, batch convert losslessly with IrfanView with the "Fine rotation: 180.00" setting.

Open all the scanned images with Photoshop and duplicate the image: we will save one for archiving purposes, and we will work on the second one.<br>
For starters, make sure the image is straightened. To straighten images, use the ruling function from the cropping tool.<br>
![EDITING 01](/Assets/Editing-straighten01.jpg)<br>

Add a leveling layer, and balance it according to the correct colours; act based on true whites & blacks. (You may use the eye dropper)<br>
Comparison [here](https://slow.pics/c/esz9kdg4).<br>
![EDITING 01](/Assets/Editing-leveling01.jpg)<br>

Add a brightness layer and set it to max so we can see things to fix.<br>
Normally, the leveling might already have fixed most of things.<br>
![EDITING 01](/Assets/Editing-brightness01.jpg)<br>

Remove the bad parts with the Brush tool / Spot healing brush tool, and "heal" the parts where there are dust.<br>
When it's done, remove the brightness layer and save as PSD.<br>
![EDITING 01](/Assets/Editing-final01.jpg)<br>




## FILTERING
TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO<br>
TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO<br>
TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO<br>



## EXPORT

### Lossless
*All lossless files are encoded from the PSD files with IrfanView.*

________________
**PNG**:<br> DPI & resolution untouched, set "compression level" to 9.<br>
![Export PNG 01](/Assets/Export-PNG01.jpg)<br>

### Lossy
________________
**WEBP**:<br> 72 DPI, 7000 height, set lossless compression, "compression method" to 6.<br>
![Export WEBP 01](/Assets/Export-WEBP01.jpg)<br>
![Export WEBP 02](/Assets/Export-WEBP02.jpg)<br>

________________
**JPG**:<br> 72 DPI, 2048 height, set quality to 100%.<br>
![Export JPG 01](/Assets/Export-JPG01.jpg)<br>
![Export JPG 02](/Assets/Export-JPG02.jpg)<br>




## FINAL
________________

Make sure to save all PSD files, and compress the folder project with 7zip.<br>
![Export PSD 01](/Assets/Export-PSD01.jpg)<br>

Final files:<br>
![FINAL](/Assets/Final.jpg)<br>
![FINAL](/Assets/04-Lossyexport.jpg)<br>
