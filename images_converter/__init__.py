from models import Image

import json
import os
import re

# CREATE IMAGE LIST:
def create_image_list(root: str, files: list, image_extensions: list) -> list:
    '''Create images list'''
    images = []
    for file in files:
        for extension in image_extensions:
            if extension in file.lower():
                images.append(Image(root = root, file = file))
                break
    return images

# LOAD CONFIGs:
config_file_path = './images_converter/config.json'
with open(config_file_path) as config_file:
    configs = json.load(config_file)
    config_file.close()

# VERIFY PATH:
if os.path.exists(configs['root']):

    # CREATE FILE LIST:
    files = os.listdir(configs['root'])

    # CREATE IMAGE LIST:
    images = create_image_list(root = configs['root'], files = files, image_extensions = configs['image_extensions'])

    # TESTs:
    for image in images:
        print(image.name, image.extension)

else:
    print("This path doesn't exist...")
