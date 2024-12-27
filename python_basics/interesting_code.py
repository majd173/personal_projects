import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    """
    Compute the Mandelbrot set for a given complex number c and maximum iterations.
    """
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

# Image size (pixels)
width, height = 800, 800
# Plot window
re_min, re_max = -2, 1
im_min, im_max = -1.5, 1.5
max_iter = 256

# Create a 2D array to store the results
image = np.zeros((height, width))

for x in range(width):
    for y in range(height):
        # Convert pixel coordinate to complex number
        c = complex(re_min + (x / width) * (re_max - re_min),
                    im_min + (y / height) * (im_max - im_min))
        # Compute the Mandelbrot set
        m = mandelbrot(c, max_iter)
        # Map the result to a color
        color = 255 - int(m * 255 / max_iter)
        image[y, x] = color

# Plot the image
plt.imshow(image, cmap='inferno', extent=(re_min, re_max, im_min, im_max))
plt.colorbar()
plt.title("Mandelbrot Set")
plt.xlabel("Re")
plt.ylabel("Im")
plt.show()
