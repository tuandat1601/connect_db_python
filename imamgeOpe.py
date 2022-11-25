import numpy as np
from imageio import imread, imwrite
from skimage.transform import resize
import matplotlib.pyplot as plt

# Read an JPEG image into a numpy array
img = imread('woman-2593366.jpg')
print(img.dtype, img.shape)  # Pri
img_tinted = (img * [1, 0.95, 0.9])
print(img_tinted.dtype, img_tinted.shape)  # Prints "float64 (400, 248, 3)"

# Resize the tinted image to be 300 by 300 pixels.
img_tinted = resize(img_tinted, (300, 300)).astype(dtype=np.uint8)
print(img_tinted.dtype, img_tinted.shape)  # Prints "uint8 (300, 248, 3)"

# Write the tinted image back to disk
imwrite('woman-2593366.jpg', img_tinted)
plt.imshow(img_tinted)
plt.show()