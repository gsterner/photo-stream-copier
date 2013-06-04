__author__ = 'Gustaf'

import photo_data
import config
import photo_utils
import directories


def get_photo_data_from_list(photo_path_list):
    return [photo_data.PhotoData(photo) for photo in photo_path_list]


def dates_from_data_list(data_list):
    return [data_object.date_taken() for data_object in data_list]


def months_from_date_list(date_list):
    return[directories.Month(date) for date in date_list]


def unique_month_directory(month_list):
    """Makes sure that the month objects are unique"""
    return dict([(month.short_name(), month) for month in month_list])


def get_months_from_files(file_list):
    data_list = get_photo_data_from_list(file_list)
    date_list = dates_from_data_list(data_list)
    month_list = months_from_date_list(date_list)
    return unique_month_directory(month_list)

photos = photo_utils.list_of_photo_paths(config.SOURCE_DIR)
photo_dict = get_months_from_files(photos)
print photo_dict