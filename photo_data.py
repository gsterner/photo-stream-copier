import pyexiv2
import datetime
import os

class PhotoData():
    def __init__(self, file_path):
        self.meta_data =pyexiv2.ImageMetadata(file_path)
        self.meta_data.read()
        self.file_path = file_path

    def date_taken(self):
        if 'Exif.Image.DateTime' in self.meta_data.keys():
            date_taken = self.meta_data['Exif.Image.DateTime']
            return date_taken.value
        else:
            time_as_ctime = os.path.getctime(self.file_path)
            return datetime.datetime.fromtimestamp(time_as_ctime)
            #print datetime.datetime.strptime(str(time_as_ctime), "%a %b %d %H:%M:%S %Y")
            return None

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