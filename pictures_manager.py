from os import listdir
from os.path import isfile, join
import sys

import piexif


pictures_directory = 'static/pictures/'


EXIF_GPS = {
    'GPSAltitude': 0x0006,
    'GPSAltitudeRef': 0x0005,
    'GPSDate': 0x001D,
    'GPSDestBearing': 0x0018,
    'GPSDestBearingRef': 0x0017,
    'GPSImgDirection': 0x0011,
    'GPSImgDirectionRef': 0x0010,
    'GPSLatitude': 0x0002,
    'GPSLatitudeRef': 0x0001,
    'GPSLongitude': 0x0004,
    'GPSLongitudeRef': 0x0003,
    'GPSSpeed': 0x000D,
    'GPSSpeedRef': 0x000C,
    'GPSTimeStamp': 0x0007,
    'Tag 0x001F': 0x001F
}


def dd_from_dms(bearing, degree, minutes, seconds):
    """
    Convert DMS (Degrees, Minutes, Seconds) coordinates to DD (Decimal Degrees)
    :param bearing: 'N'
    :param degree: (37, 1)
    :param minutes: (3803, 100)
    :param seconds: (29, 1)
    :return:
    """
    sign = 1 if bearing in ['N', 'E'] else -1
    return sign * (degree[0] / degree[1] + minutes[0] / minutes[1] / 60 + seconds[0] / seconds[1] / 3600)


def load_pictures():
    pictures = []
    for file in listdir(pictures_directory):
        file_path = join(pictures_directory, file)
        if not isfile(file_path):
            continue
        exif = piexif.load(file_path)
        latitude = dd_from_dms(
            exif['GPS'][EXIF_GPS['GPSLatitudeRef']].decode('utf-8'),
            *exif['GPS'][EXIF_GPS['GPSLatitude']])
        longitude = dd_from_dms(
            exif['GPS'][EXIF_GPS['GPSLongitudeRef']].decode('utf-8'),
            *exif['GPS'][EXIF_GPS['GPSLongitude']])
        pictures.append((file_path, latitude, longitude))
    return pictures

