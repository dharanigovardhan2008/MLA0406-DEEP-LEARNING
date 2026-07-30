from google.colab import files
uploaded = files.upload()
from PIL import Image
import numpy as np

image_path = list(uploaded.keys())[0]

img = Image.open(image_path)
pixels = np.array(img)

print("Image Shape:", pixels.shape)
print("\nPixel Values:")
print(pixels)
