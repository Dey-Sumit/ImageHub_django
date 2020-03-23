from PIL import Image, ExifTags
import os

class EXIF():
    def __init__(self, image):
        #self.image = image.replace('/', '\\')
        #ROOT_DIR_1 = os.path.dirname(os.path.abspath(__file__))
        #self.img = os.path.dirname(ROOT_DIR_1) + self.image
        self.img = image
        print("from exif.py ")
    def get_exif_data(self):
        img = Image.open(self.img)

        img_exif = img._getexif()
        if img_exif is None:
            return "No exif Data"
        else:
            exif = {
                ExifTags.TAGS[k]: v
                for k, v in img._getexif().items()
                if k in ExifTags.TAGS
            }
            return exif