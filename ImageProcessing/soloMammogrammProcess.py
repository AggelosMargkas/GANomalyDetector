# Se auto to .py tha ksekinisoume na epireazoume mono mia mastografia
# that paroyme mia periptwsi pou den einai normal kai peiexei lession
# kai maska.

# 1. metatropi se png.
# 2. Apply NYU

import cv2 as cv
import os
import pydicom
import matplotlib.image as image
from NYU_crop_single_mammogram import crop_mammogram_one_image
import matplotlib.pyplot as plt
from PIL import Image

# mask = image.imread(    'C:/Users/junio/Desktop/Thesis/CBIS_DDSM_Image_Processing/manifest-1667899688383/CBIS-DDSM/Calc-Training_P_01647_RIGHT_MLO_1/1-2.png')

scan = {"horizontal_flip": "YES", "side": "R"}
print(scan)


def plot_morphological_changes():
    """
        Plots 3 couples of images and the effect that the morphological processing of NYU has on the
        digitized CBIS-DDSM
    """
    img1 = image.imread(
        r'C:/Users/junio/Desktop/Thesis/CBIS_DDSM_Image_Processing/manifest-1667995631662/CBIS-DDSM/Calc-Test_P_00038_LEFT_CC/image.png')
    img2 = image.imread(
        r"C:\Users\junio\Desktop\Thesis\CBIS_DDSM_Image_Processing\outputImages\cropped_image1.png")
    img3 = image.imread(
        r"C:\Users\junio\Desktop\Thesis\CBIS_DDSM_Image_Processing\manifest-1667995631662\CBIS-DDSM\Calc-Test_P_00077_LEFT_CC\anotherimage.png")
    img4 = image.imread(
        r"C:\Users\junio\Desktop\Thesis\CBIS_DDSM_Image_Processing\outputImages\cropped_image2.png")
    img5 = image.imread(
        r"C:\Users\junio\Desktop\Thesis\CBIS_DDSM_Image_Processing\manifest-1667899688383\CBIS-DDSM\Calc-Training_P_01647_RIGHT_MLO\image.png")
    img6 = image.imread(
        r"C:\Users\junio\Desktop\Thesis\CBIS_DDSM_Image_Processing\outputImages\cropped_image.png")

    hist_full_normal = cv.calcHist([img1], [0], None, [256], [0, 256])

    f, axarr = plt.subplots(3, 3)
    axarr[0, 0].imshow(img1, cmap='gray')
    axarr[0, 1].imshow(img2, cmap='gray')
    axarr[0, 2].plot(hist_full_normal)
    axarr[1, 0].imshow(img3, cmap='gray')
    axarr[1, 1].imshow(img4, cmap='gray')
    axarr[1, 2].imshow(img2, cmap='gray')
    axarr[2, 0].imshow(img5, cmap='gray')
    axarr[2, 1].imshow(img6, cmap='gray')
    axarr[2, 2].imshow(img2, cmap='gray')

    plt.show()


plot_morphological_changes()


def dicomTOpng():

    # main path to CBIS-DDSM
    inputdir = r'C:/Users/junio/Desktop/Thesis/CBIS_DDSM_Image_Processing/manifest-1667995631662/CBIS-DDSM'

    # get all possible image paths
    test_list = [f for f in os.listdir(inputdir)]

    # init full path list
    img_path_list = []

    for file in test_list[:1]:
        img_path = inputdir + "/" + file
        for i in os.listdir(img_path):
            img_path_list.append(img_path + '/' + i)

    for f in img_path_list:

        ds = pydicom.read_file(f)
        img = ds.pixel_array
        cv.imwrite(f.replace('.dcm', '.png'), img)
