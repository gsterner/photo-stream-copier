import pyexiv2
import datetime

#metadata = pyexiv2.ImageMetadata('"C:\Users\Gustaf\Pictures\Photo Stream\My Photo Stream\IMG_2882.JPG"')
metadata = pyexiv2.ImageMetadata('IMG_2882.JPG')
metadata.read()
for k in metadata.exif_keys: print k

model = metadata['Exif.Image.Model']
date_taken = metadata['Exif.Image.DateTime']

today = datetime.datetime.today()
print date_taken.value > today

print 'Exif.Image.Model' in metadata