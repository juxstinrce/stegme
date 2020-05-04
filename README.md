# stegme
A hand-crafted method of steganography

`stegme.py` is the file that allows you to hide data in an image.<br>
`solve.py` is the file that allows you to retrieve the hidden data.<br>

# How it works
- The file `steg.py` opens your image
- Encode data in binary
- Selects one pixel per bit
- Randomly chooses the pixel to be modified (R, G or B) 
- Increments it by 1 if the bit is equal to 1, or decrements it by 1 if the bit is equal to 0
- Finally, it displays the "key", which contains all the pixels that have been altered.

`solve.py` needs the original image to extract hidden data.

It is impossible to recover the data in the image without the key.
