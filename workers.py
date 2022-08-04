from celery import Celery
from PIL import Image
import os
#replace broker with rabbit mq
celery = Celery("workers", broker="redis://localhost")


#test the worker
@celery.task
def run_work():
    return "hello i'm running"




#upload to cloud
@celery.task
def size_reducer(filename):
    size = (24, 24)
    with Image.open(filename) as img:
        new_image = img.resize(size)
        new_image.save("fortnite-resized.jpeg")
        print(f"image_size:{new_image} previous {img.size}")
    curr_path = os.getcwd()
    os.remove(path=f"{curr_path}/{filename}")

