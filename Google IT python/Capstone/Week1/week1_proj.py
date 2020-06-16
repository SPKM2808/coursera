#! /usr/bin/env python3
import os
from PIL import Image

files=os.walk(os.getcwd()+'/images')

for a,b,i in files:
        for x in i:
                if x.startswith('ic'):

                        im=Image.open(a+'/'+x).convert("RGB")
                        im.rotate(270).resize((128,128)).save('/home/student-00-56f8b56647d7/opt/icons/'+x,"JPEG")
