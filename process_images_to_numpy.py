import numpy as np
import csv
import cv2
import os


def readLines(filename):
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        lines = []
        for line in reader:
            lines.append(line)

    return lines

def saveImagesData(csv_filename, dir_to_save):
    lines = readLines(csv_filename)

    image_dir = os.path.dirname(csv_filename)

    center_images = []
    left_images = []
    right_images = []
    directions = []

    for line in lines:
        if line[3] != 'steering':
            center_filename = os.path.join(
                image_dir, 'IMG', line[0].split('/')[-1])
            left_filename = os.path.join(image_dir, 'IMG', line[1].split('/')[-1])
            right_filename = os.path.join(image_dir, 'IMG', line[2].split('/')[-1])

            center_images.append(cv2.imread(center_filename))
            left_images.append(cv2.imread(left_filename))
            right_images.append(cv2.imread(right_filename))
            directions.append(float(line[3]))

    X_center = np.array(center_images)
    X_left = np.array(left_images)
    X_right = np.array(right_images)
    y = np.array(directions)

    np.save(os.path.join(dir_to_save, 'y'), y)
    np.save(os.path.join(dir_to_save, 'X_center'), X_center)
    np.save(os.path.join(dir_to_save, 'X_left'), X_left)
    np.save(os.path.join(dir_to_save, 'X_right'), X_right)


# image_root = '../behavioral_cloning_images' # on personal computer
image_root = '../data'  # on udacity project
dir_to_save = '/opt/'

csv_files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(
    image_root) for f in filenames if os.path.splitext(f)[1] == '.csv']

for file in csv_files:
    dir_name =  dir_to_save + os.path.dirname(file).split('/')[-1]
    if not(os.path.exists(dir_name)):
        print('Processing images from file: ', file)
        os.mkdir(dir_name)
        saveImagesData(file, dir_name)
        print('File saves on directory: ', dir_name)
    else:
        print('Images from file ', file, ' were already processed')
        
# loading course sample data
file = './data/driving_log.csv'
dir_name = '/opt/sample_data'
csv_files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(
    image_root) for f in filenames if os.path.splitext(f)[1] == '.csv']   

if not(os.path.exists(dir_name)):
    os.mkdir(dir_name)
    print('Processing images from file: ', file)
    saveImagesData(file, dir_name)
    print('File saves on directory: ', dir_name)
else:
    print('Sample images already processed')