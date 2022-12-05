from os import listdir
from os.path import isfile, join
import os
import cv2 as cv
import matplotlib.pyplot as plt


def get_filepaths(directory):
    """
    This function will generate the file names in a directory 
    tree by walking the tree either top-down or bottom-up. For each 
    directory in the tree rooted at directory top (including top itself), 
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.

    return file_paths  # Self-explanatory.


# Run the above function and store its results in a variable.
full_file_paths = get_filepaths("/Users/johnny/Desktop/TEST")
onlyfiles = get_filepaths(
    r"C:\Users\junio\Desktop\Thesis\CBIS_DDSM_Image_Processing\fullMammogramsConvertedToPng")


for i in range(0, 10, 2):

    normal_file = onlyfiles[i]
    #print(normal_file + " =========")
    processed_file = onlyfiles[i+1]
    #print(onlyfiles[i+1] + " *************")
    img_normal = cv.imread(normal_file, 0)
    print(img_normal)
    img_proc = cv.imread(processed_file, 0)
    print(img_proc)
    fig, ax = plt.subplots(2, 2)
    #hist = cv.calcHist(img)
    hist_full_normal = cv.calcHist([img_normal], [0], None, [255], [10, 400])
    hist_full_proc = cv.calcHist([img_proc], [0], None, [255], [10, 400])
    ax[0, 0].plot(hist_full_normal)
    ax[0, 0].set_title("Original")
    ax[0, 1].plot(hist_full_proc)
    ax[0, 1].set_title("Filtered")

    ax[1, 0].imshow(img_normal)
    ax[1, 0].set_title("Original")
    ax[1, 1].imshow(img_proc)
    ax[1, 1].set_title("Filtered")
    plt.xlim([0, 256])

plt.show()
