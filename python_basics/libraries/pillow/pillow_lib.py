from PIL import ImageGrab

# Take a screenshot of the entire screen
screenshot = ImageGrab.grab()

# Get the size of the screenshot
width, height = screenshot.size
print(f"Screenshot width: {width}, height: {height}")

pixel_color = screenshot.getpixel((100, 100))
print(f"Pixel color at (100, 100): {pixel_color}")