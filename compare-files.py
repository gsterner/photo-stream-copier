import os
import filecmp

photo_stream_path = "C:\\Users\\Gustaf\\Pictures\\Photo Stream\\My Photo Stream"
photo_stream_list = os.listdir(photo_stream_path)

destination_path = "C:\\Users\\Gustaf\\Documents\\lisas-iphone-foton\\800AAAAA"
destination_list = os.listdir(destination_path)

count = 0
for photo in photo_stream_list:
    if photo in destination_list:
        stream_photo = photo_stream_path + "\\" + photo
        dest_photo = destination_path + "\\" + photo
        count += 1
        print photo, filecmp.cmp(stream_photo, dest_photo)
#print filecmp.cmp(dl[0], dl[1])
print count
print len(destination_list)
#os.path.exists('z:')