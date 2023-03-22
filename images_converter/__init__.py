import json
import os
import re

def images(files: list, image_extensions: list) -> dict:
    '''Return only images in a list of files'''
    images = {}
    for file in files:
        file = file.lower()
        for extension in image_extensions:
            if extension in file:
                images.update({file : extension})
    return images

# LOAD CONFIGs:
config_file_path = './images_converter/config.json'
with open(config_file_path) as config_file:
    configs = json.load(config_file)
    config_file.close()

# Verify path:
if os.path.exists(configs['images_path']):
    # Create file list:
    files = os.listdir(configs['images_path'])
    # Create dict {file : extension} with all images
    image_files = images(files, configs['image_extensions'])
    print(image_files)
else:
    print("This path doesn't exist...")
