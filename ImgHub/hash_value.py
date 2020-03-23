import imagehash
from PIL import Image

def get_hash(imageFile):
    image = Image.open(imageFile)
    dhash_value = imagehash.dhash(image)
    return str(dhash_value)
