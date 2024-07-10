import matplotlib.pyplot as plt
from matplotlib import image as mpimg
from skimage import color, restoration
import numpy as np
def run_cel_shader(img):

    print("Running Cel_shader try #1")
    image = mpimg.imread('a.png')
    plt.imshow(image)
    plt.show()

if __name__ == "__main__":
    filename = "a.png"
    run_cel_shader(filename)
