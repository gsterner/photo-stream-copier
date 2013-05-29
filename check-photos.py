import os
import pyexiv2

photo_stream_path = "C:\\Users\\Gustaf\\Pictures\\Photo Stream\\My Photo Stream\\"
photo_stream_list = os.listdir(photo_stream_path)
model_names = ['iPhone 4', 'iPhone 5', 'iPhone 3GS', 'iPad']
#photo_name = 'IMG_2882.JPG'

for photo_name in photo_stream_list:
    metadata = pyexiv2.ImageMetadata(photo_stream_path + photo_name)
    metadata.read()
    if 'Exif.Image.Model' in metadata:
        model = metadata['Exif.Image.Model']
        if model.value not in model_names:
            print 'model', model, photo_name

    else:
        print 'no model'

