__author__ = 'Gustaf'

import os
import photo_data
import config

photo_list = os.listdir(config.SOURCE_DIR)

#photo_path_list =
data_list = [photo_data.PhotoData(photo) for photo in photo_list]

print data_list