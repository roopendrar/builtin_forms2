import os
os.environ.setdefault("DANGO_SETTINGS_MODULE","APP11.settings")

import django
django.setup()

from django.core.files.storage import FileSystemStorage


def store_img(image):
    fs=FileSystemStorage()
    file=fs.save(image.name,image)
    file_url=fs.url(file)
    return file_url