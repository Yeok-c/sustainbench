import glob, os
import numpy as np
import matplotlib.pyplot as plt
street_level_image_root = r"C:/UCL Coursework/Sem 1/COMP0173/sustainbench/dhs/mapillary/imagery/"
zip_files = glob.glob(f'{street_level_image_root}/*.zip')

for zip_file in zip_files:
    print(f'Unzipping {zip_file}...')
    os.system(f'unzip \"{zip_file}\" -d \"{street_level_image_root}\"')