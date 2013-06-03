import shutil
import os

__author__ = 'Gustaf'

SOURCE_DIR = "C:\\Users\\Gustaf\\Documents\\photo-test\\source"
DESTINATION_DIR = "C:\\Users\\Gustaf\\Documents\\photo-test\\destination"
SLASH = '\\'


def copy_photo(source_dir, dest_dir, file_name):
    file_path_source = source_dir + SLASH + file_name
    file_path_dest = dest_dir + SLASH + file_name
    shutil.copyfile(file_path_source, file_path_dest)


def join_directory_file_name(directory, file_name):
    return directory + SLASH + file_name