import pyexiv2
import datetime


class PhotoData():
    def __init__(self, filePath):
        self.meta_data =pyexiv2.ImageMetadata(filePath)
        self.meta_data.read()

    def date_taken(self):
        date_taken = self.meta_data['Exif.Image.DateTime']
        return date_taken.value

"""
#metadata = pyexiv2.ImageMetadata('"C:\Users\Gustaf\Pictures\Photo Stream\My Photo Stream\IMG_2882.JPG"')
metadata = pyexiv2.ImageMetadata('IMG_2882.JPG')
metadata.read()
for k in metadata.exif_keys: print k

model = metadata['Exif.Image.Model']
date_taken = metadata['Exif.Image.DateTime']

today = datetime.datetime.today()
print date_taken.value > today

print 'Exif.Image.Model' in metadata
"""