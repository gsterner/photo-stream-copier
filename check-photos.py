import os
import pyexiv2

photo_stream_path = "C:\\Users\\Gustaf\\Pictures\\Photo Stream\\My Photo Stream\\"
photo_stream_list = os.listdir(photo_stream_path)

#photo_name = 'IMG_2882.JPG'

for photo_name in photo_stream_list:
	metadata = pyexiv2.ImageMetadata(photo_stream_path+photo_name)
	metadata.read()
	if 'Exif.Image.Model' in metadata:
		model = metadata['Exif.Image.Model']
		if model.value != 'iPhone 4':
			print 'model', model
		
	else :
		print 'no model'

