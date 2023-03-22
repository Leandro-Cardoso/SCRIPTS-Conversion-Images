import json

# LOAD CONFIGs:
config_file_path = './images_converter/config.json'
with open(config_file_path) as config_file:
    configs = json.load(config_file)
    config_file.close()
