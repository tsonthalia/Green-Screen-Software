
import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
import sys

#path to background images
backgroundPath = 'images/backgrounds'

#path to result image folder
resultPath = 'images/result/'

#path to images that needs to be stripped of backgrounds
hardwarePath = 'images/hardware'

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()

for currentBolt in os.listdir(hardwarePath):
    print("Starting " + currentBolt)
    imagesPath = 'images/hardware/' + currentBolt
    resultImagesPath = 'images/result/' + currentBolt
    count = 0
    if currentBolt not in os.listdir(resultPath):
        printProgressBar(0, len(os.listdir(backgroundPath)) * len(os.listdir(imagesPath)), prefix = 'Progress:', suffix = 'Complete', length = 50)
        os.mkdir(resultImagesPath)
        for currBackgroundImage in os.listdir(backgroundPath):
            for entry in os.listdir(imagesPath):
                extension = os.path.splitext(entry)[1]
                if os.path.isfile(os.path.join(imagesPath, entry)) and os.path.splitext(entry)[1] == '.JPG':
                    image = cv2.imread(os.path.join(imagesPath, entry))

                    image_copy = np.copy(image)

                    image_copy = cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB)

                    # THE COLORS BELOW ARE TEMPLATES FOR OTHER COLOR BACKGROUNDS
                    # UNCOMMENT THEM IN ORDER TO USE THAT COLOR INSTEAD
                    # YOU CAN FINE-TUNE THE COLOR BY CHANGING THE LOWER AND UPPER RANGE OF THE COLOR

                    # GREEN
                    # lower_green = np.array([0, 100, 0])
                    # upper_green = np.array([180, 255, 170])
                    # mask = cv2.inRange(image_copy, lower_green, upper_green)

                    # WHITE
                    # lower_white = np.array([180, 180, 180])
                    # lower_white = np.array([120,120,120])
                    # upper_white = np.array([255, 255, 255])
                    # Define the masked area
                    # mask = cv2.inRange(image_copy, lower_white, upper_white)

                    # WOOD
                    # lower_wood = np.array([130,120,100])
                    # upper_wood = np.array([255, 255, 255])
                    # mask = cv2.inRange(image_copy, lower_wood, upper_wood)


                    # PURPLE
                    # lower_purple = np.array([100,80,100])
                    # upper_purple = np.array([255, 200, 255])
                    # mask = cv2.inRange(image_copy, lower_purple, upper_purple)

                    # BLUE
                    # lower_blue = np.array([0,50,100])
                    # upper_blue = np.array([100, 160, 255])
                    # mask = cv2.inRange(image_copy, lower_blue, upper_blue)

                    # OVERHEAD PROJECTOR
                    lower_overhead = np.array([90, 60, 30])
                    upper_overhead = np.array([255, 255, 255])
                    mask = cv2.inRange(image_copy, lower_overhead, upper_overhead)

                    masked_image = np.copy(image_copy)
                    masked_image[mask != 0] = [0, 0, 0]

                    background_image = cv2.imread(os.path.join(backgroundPath, currBackgroundImage))
                    background_image = cv2.cvtColor(background_image, cv2.COLOR_BGR2RGB)

                    crop_background = background_image[0:image.shape[0], 0:image.shape[1]]

                    crop_background[mask == 0] = [0, 0, 0]

                    final_image = crop_background + masked_image

                    cv2.imwrite(os.path.join(resultImagesPath, currentBolt + '_' + str(count) + '.jpeg'), final_image)

                    count+=1

                    printProgressBar(count+1, len(os.listdir(backgroundPath)) * len(os.listdir(imagesPath)), prefix = 'Progress:', suffix = 'Complete', length = 50)
        print("")
        print("Completed images for " + currentBolt)
    else:
        print(currentBolt + " has already been done.")
