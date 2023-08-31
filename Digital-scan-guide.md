#  A guide to make your scanned illustration look like a digital file


Yep, just as the title says.<br>
A lot of illustrations are actually being gatekept in various expensive or limited magazines, resulting in a mass list of work considered "lost medias".<br>
Inspired from the work of [Drop](https://yande.re/user/show/188377), I am going to show you may way of transforming some random, raw scan into a beautiful, clean digital file.<br>

First of all, you might want your scan to be in the highest resolution possible. In my case, I like to go with **1600dpi**, where the resolution of an **A4** page would be **13599 x 18719 px**.<br>
With that said, it is time to import the scan into photoshop.<br>

Of course, straightening the image and cropping it right at the beginning is a must.<br>
![DIGITAL 01](/Assets/Digital-001.jpg)<br>


Now then, let's not forget about leveling the scan. More info about leveling can be found in my main guide.<br>
![DIGITAL 02](/Assets/Digital-002.jpg)<br>

A crucial part of the process is removing all the dust, scratches & various nuisances with the healing brush tool.<br>
![DIGITAL 03](/Assets/Digital-003.jpg)<br>

With that done, we will need to start to remove the colour noise, artefact caused by scanning.<br>
A before/after comparison of this step can be found [here](https://slow.pics/c/hWlLhpTd).<br>
![DIGITAL 04](/Assets/Digital-004.jpg)<br>

Finally, let's start preparing for the final process.<br>
What we will need to do is rescale our absurd-res scan into something the web.<br>
I like to go with **6000px** for the height and **96DPI**, rescaling with **Bicubic sharper** for a better lineart.<br>
![DIGITAL 05](/Assets/Digital-005.jpg)<br>


Now, onto the most crucial step of our process. We will try to denoise the scanning artefects whilst keeping the lineart intact. (Careful NOT to mix this with descreening!)<br>
For this step, we will generate a lineart mask with [Vapoursynth](https://github.com/vapoursynth/vapoursynth)'s vsmasktools edgemask function "[KirschTCanny](https://vsmask.encode.moe/en/latest/api.html#vsmask.edge.KirschTCanny)".<br>

```python
import vapoursynth as vs
import vsmasktools as vmt
core = vs.core

clip = core.imwri.Read("i-005 copy.jpg")


for i in range(0, 8):
	mask = vmt.KirschTCanny.edgemask(clip, lthr=50 / 255, hthr=150 / 255, planes=i)

	inv_mask = mask.std.Invert()
	bin_mask = inv_mask.std.Binarize(1)
	nib_mask = core.std.ShufflePlanes(bin_mask, 0, vs.GRAY)

	nib_mask.set_output(i)

```

The TL;DR of this code is:<br>
• We load a a JPG export of the image into Vapoursynth<br>
• We set a range of planes to see which one yeilds the best result from the edgemask function<br>
• We binarize the output so we can simply copy paste the result into PS, as a mask<br>
• The script has to be previewed with [vspreview](https://github.com/Irrational-Encoding-Wizardry/vs-preview)<br>

And voilà!<br>
![DIGITAL 06](/Assets/Digital-006.jpg)<br>


With that done, now all we need to do is import the output as a mask for the denoise.<br>
This mask will help us keep our lineart intact from denoising.<br>
To do so, here are the steps:<br>
• Import the output into PS. CTRL+A, CTRL+C<br>
• Add a mask to the smart-object layer we will denoise. ALT+click on the mask<br>
• CTRL+V<br>
![DIGITAL 07](/Assets/Digital-007.jpg)<br>
![DIGITAL 08](/Assets/Digital-008.jpg)<br>


Finally, use the denoiser of your choice directly within PS, and you're done!<br>
![DIGITAL 09](/Assets/Digital-009.jpg)<br>

Here are some comparison of the results:<br>
• https://slow.pics/c/xiuqfSt5<br>
• https://slow.pics/c/Bmn514Fq<br>
