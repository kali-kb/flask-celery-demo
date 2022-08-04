from PIL import Image
import os

def image_resizer():
    image = "path-to-image"
    name = "unknown"
    with Image.open(image) as img:
        new_image = img.resize((24,24))
        new_image.save(f"{name}.jpeg")
        print(f"image_size:{new_image} previous {img.size}")
    curr_path = os.getcwd()
    return curr_path

    # img = Image.open("fortnite.jpg")
# img1 = Image.open("fortnite.jpg")
# img1.show()

image_resizer()