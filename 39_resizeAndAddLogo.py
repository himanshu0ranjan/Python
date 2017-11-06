'''
Created on Jul 28, 2017

@author: Himanshu Ranjan
'''
import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'C:\\PythonExFiles\\automate_online-materials\\catlogo1.png'


logoIm = Image.open(LOGO_FILENAME)
#logoIm = logoIm1.resize((100,100))
#logoIm.save('C:\\PythonExFiles\\automate_online-materials\\catlogo1.png')
logoWidth, logoHeight = logoIm.size 

print(logoWidth, logoHeight)

# Make a destination directory in the designated directory
os.makedirs('withlogo', exist_ok=True)

# Loop over all the files in the designated directory
for filename in os.listdir('C:\\PythonExFiles\\automate_online-materials'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) \
       or os.path.join('C:\\PythonExFiles\\automate_online-materials', filename) == LOGO_FILENAME:
        continue # skip non-image files and the logo file itself
    
    im = Image.open(os.path.join('C:\\PythonExFiles\\automate_online-materials', filename))
    width, height = im.size 
    
        
    # check if image needs to be resized
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        #print(width, height)
        # Calculate the new width and height to resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE/ width) * height)
            width = SQUARE_FIT_SIZE
            
        else:
            width = int((SQUARE_FIT_SIZE/ height) * width)
            height = SQUARE_FIT_SIZE
            
        # Resize the image
        print('Resizing %s...' % (filename))
        im = im.resize((width,height))
        
        #print(width, height)
        # Add the logo
        print('Adding logo to %s...' % (filename))
        im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)
        
        # Save changes
        im.save(os.path.join('withlogo', filename))

