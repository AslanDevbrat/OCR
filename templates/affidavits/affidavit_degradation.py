

from degradation import degrade
import numpy as np
import pdf2image

img = pdf2image.convert_from_path("./affidavit_latex.pdf")

img[0].save('affidavit_latex.jpg')

degrade = degrade()

img = degrade.read("affidavit_latex.jpg")

stamp = degrade.read("stamps/circular_stamp.png")
stamp2 = degrade.read("stamps/rectangle_tamil-removebg.png")
stamp2 = degrade.dilate(stamp2, np.ones((5,1),np.uint8))
stamp = degrade.dilate(stamp, np.ones((4,1),np.uint8))
stamp3 = degrade.read("stamps/rectangle.png")
text = degrade.read("stamps/random_text-removebg-preview.png")
stamp3 = degrade.dilate(stamp3, np.ones((2,1), np.uint8))
newimg = degrade.dilate(img, np.ones((5, 9), np.uint8))
newimg = degrade.stamp(img, stamp, rotate_angle=45, scale_percent=80, pos=[200, 1850])

newimg = degrade.salt(newimg)

newimg = degrade.stamp(newimg, stamp3, rotate_angle=-10, scale_percent= 90, pos = [900, 700])

#newimg = degrade.stamp(newimg,text, rotate_angle = 8, scale_percent = 80, pos = [400, 900] )

newimg = degrade.pepper(newimg, amount=0.001)
newimg = degrade.blur(newimg, radius=4)

newimg = degrade.stamp(newimg, stamp2, rotate_angle=5, scale_percent = 70, pos= [1200, 1900])

newimg = degrade.rotate(newimg, -0.9)
degrade.save(newimg, "affidavit_latex_modified.jpg")


