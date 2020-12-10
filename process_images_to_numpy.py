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


def saveImagesData(csv_filename):
    lines = readLines(csv_filename)

    image_dir = os.path.dirname(csv_filename)

    center_images = []
    left_images = []
    right_images = []
    directions = []

    for line in lines:
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

    np.save(os.path.join(image_dir, 'X_center'), X_center)
    np.save(os.path.join(image_dir, 'X_left'), X_left)
    np.save(os.path.join(image_dir, 'X_right'), X_right)


# image_root = '../behavioral_cloning_images' # on personal computer
image_root = '../data'  # on udacity project

csv_files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(
    image_root) for f in filenames if os.path.splitext(f)[1] == '.csv']

for file in csv_files:
    saveImagesData(file)
