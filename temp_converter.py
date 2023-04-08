import cv2
import os
import pydicom
import numpy as np

"""

TODO: 1. Solve interprentation of print.
      2. Fix error of created png photos.
      3. If img not png => convert => save.
      4. fix requirements in general.
"""

inputdir = '/home/amargkas/VinDR/physionet.org/files/vindr-mammo/1.0.0/images'
outdir = './'
# os.mkdir(outdir)

test_list = [f for f in os.listdir(inputdir)]


def clear_html_files(inputdir):
    """Used this function to clear index.html files included in every patients file

    Args:
        inputdir (str): given the string of the directory it deletes all the files with
                        .html extension.
    """
    for f in test_list:   # remove "[:10]" to convert all images

        # print(f)
        mammogrammsdir = inputdir + '/' + f
        test = os.listdir(mammogrammsdir)
        print(mammogrammsdir)

        for item in test:
            if item.endswith(".html"):
                print('Hello')
                os.remove(os.path.join(mammogrammsdir, item))


def convert_to_png(inputdir):
    """Used this function to convert the dicom files to png.

    Args:
        inputdir (str): The folder of the mammograms of VinDR dataset.
    """

    for f in test_list:   # remove "[:10]" to convert all images

        print(f)
        mammogrammsdir = inputdir + '/' + f
        test = os.listdir(mammogrammsdir)
        print(mammogrammsdir)

        for item in test:

            print(item)
            if item.endswith(".dicom"):

                ds = pydicom.read_file(
                    mammogrammsdir + '/' + item)  # read dicom image
                img = ds.pixel_array  # get image array

                img = np.array(img, dtype=float)
                img = (img - img.min()) / (img.max() - img.min()) * 255.0
                img = img.astype(np.uint8)

                cv2.imwrite(mammogrammsdir + '/' + item.replace('.dicom', '.png'),
                            img)  # write png image


if __name__ == '__main__':

    convert_to_png(inputdir)
    # clear_html_files(inputdir)
    # print(test_list[0:5])**5
