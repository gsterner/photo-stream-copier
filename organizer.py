__author__ = 'Gustaf'

import os
import photo_data
import config
import photo_utils
import directories

photo_list = os.listdir(config.SOURCE_DIR)

photo_path_list = [photo_utils.join_directory_file_name(config.SOURCE_DIR, file_name) for file_name in photo_list]

data_list = [photo_data.PhotoData(photo) for photo in photo_path_list]

date_list = [data_object.date_taken() for data_object in data_list]

month_list = [directories.Month(date) for date in date_list]

#The followong makes sure that the month objects are unique
month_dictionary = dict([(month.short_name(), month) for month in month_list])

print month_dictionary