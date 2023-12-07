import os
from PIL import Image
import piexif


def process_images(folder_path):
    output_list = []

    for filename in os.listdir(folder_path):
        image_path = os.path.join(folder_path, filename)

        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            image = Image.open(image_path)

            if 'exif' in image.info:
                exif_data = piexif.load(image.info['exif'])
                gps_data = exif_data["GPS"]

                lat = gps_data[piexif.GPSIFD.GPSLatitude]
                lat_ref = gps_data[piexif.GPSIFD.GPSLatitudeRef]
                long = gps_data[piexif.GPSIFD.GPSLongitude]
                long_ref = gps_data[piexif.GPSIFD.GPSLongitudeRef]

                # convert latitude to decimal degree
                lat_dec = float(lat[0][0]) / float(lat[0][1]) + \
                          (float(lat[1][0]) / float(lat[1][1])) / 60 + \
                          (float(lat[2][0]) / float(lat[2][1])) / 3600

                if lat_ref == b'S':
                    lat_dec = -lat_dec

                # convert longitude to decimal degree
                long_dec = float(long[0][0]) / float(long[0][1]) + \
                           (float(long[1][0]) / float(long[1][1])) / 60 + \
                           (float(long[2][0]) / float(long[2][1])) / 3600

                if long_ref == b'W':
                    long_dec = -long_dec

                # Replace backslashes with forward slashes in the image path
                image_path = image_path.replace("\\", "/")

                output_list.append([lat_dec, long_dec, image_path])

    return output_list
