import sys
from PIL import Image,ImageOps
import os
if len(sys.argv)>3:
    sys.exit("Too many command-line arguments")
try:
    input=sys.argv[1]
    output=sys.argv[2]
except IndexError:
    sys.exit("Too few command-line arguments")
_,input_ext=os.path.splitext(input)
_,output_ext=os.path.splitext(output)
if not (input_ext==".jpg" or input_ext==".jpeg" or input_ext==".png"):
    sys.exit("invalid input")
if not (output_ext==".jpg" or output_ext==".jpeg" or output_ext==".png"):
    sys.exit("invalid output")
if input_ext!=output_ext:
    sys.exit("Input and output have different extensions")
try:
    shirt=Image.open("shirt.png")
    with Image.open(input)as input_img:
        img=ImageOps.fit(input_img,shirt.size)
        img.paste(shirt,shirt)
        img.save(output)



except FileNotFoundError:
    sys.exit("Input does not exist")


