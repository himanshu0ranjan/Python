'''
Created on Jul 28, 2017

@author: Himanshu Ranjan
'''
import os
from PIL import Image

actIm = Image.open('actress1.jpg')
print(actIm.size)
width, height = actIm.size
print(width)
print(height)
print(actIm.filename)
print(actIm.format, actIm.format_description)
actIm.save('actress2.png')

newIm1 = Image.new('RGBA', (100,200), 'purple')
newIm1.save('purpleImage.png')
newIm2 = Image.new('RGBA', (50,50))
newIm2.save('transparentImage.png')

croppedIm = actIm.crop((500,600,1200,1000))
croppedIm.save('croppedImage.jpg')

croppedCopyIm = croppedIm.copy()
croppedCopyIm.save('croppedCopyImage.jpg')

croppedCopyIm.paste(newIm1, (380,140))
croppedCopyIm.save('pasted.png')

croppedCopyIm.rotate(90).save('rotatedImg.png')

croppedCopyIm.rotate(6).save('rotatedImg6.png')

croppedCopyIm.rotate(6, expand=True).save('rotatedImg6_expanded.png')

croppedCopyIm.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
croppedCopyIm.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')