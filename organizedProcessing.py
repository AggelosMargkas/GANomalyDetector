"""

Okay, here we are going to combine the technics of NYU to compare mammograms
of the CBIS-DDSM dataset. The steps we have to develop are.

    1. Import some jpeg images and plot their histograms. (done)
    2. Crop these jpeg and plot their histogram. (done)
    3. Add them in couples both the pro and post versions, try to do this in the same format. (not-done)
    4. Learn how to plot and compare them. (done)


NOTE: This programm is not really scalable. Is mostly focused on generic paths.
      
      Need to create a file with well organised coupled of image and their processed versions.
      Seems not to have proble with the cv2 and mahotas on ploting jpg and png images. Both
      work well for now. However, due to the errores on the past it is highly recommended to
      convert them to png.

      Plus, it will be really helpful to implement the CBIS-DDSM library straight from the official
      link of cancer dataset. Thus, you can implement the DICOM conversition and directly to png.

TODO: 1. I have cleaned the png files on the fullMammogramm folder. Try to create a file with coupled of images
         processed with the NYU and in their folder add the processed images of Psarakis.
        
      2. Compare the process.

      3. See ways that you can make the matlab code more applicable and not so brute force.

"""
import cv2
from matplotlib import pyplot as plt
from NYU_crop_single_mammogram import crop_mammogram_one_image
import mahotas
import numpy
import matplotlib.pyplot as plt

# vector arranging the transformation of the image, needed on the NYY library.
scan = {"horizontal_flip": "NO", "side": "R"}


def import_and_plot_histogramm(image_path, image__processed_path):
    """
    Given the image path this function opens it and returns the histogram.
    Because all the images have high intensities of 0(blacks), I plot the histogramm
    strarting from 1. The range can be processed in the function calcHist.

    Args:
        image_path (str): path of the image to plot.

    """
    img_normal = cv2.imread(image_path)
    img_processed = cv2.imread(image__processed_path)
    # computing the histogram of the blue channel of the image
    hist1 = cv2.calcHist([img_normal], [0], None, [256], [10, 256])
    hist2 = cv2.calcHist([img_processed], [0], None, [256], [10, 256])
    hist3 = cv2.calcHist([img_normal], [0], None, [256], [0, 256])
    hist4 = cv2.calcHist([img_processed], [0], None, [256], [0, 256])

# FIGURE 1

    plt.figure()

    # Plot 1

    plt.subplot(2, 2, 1)

    plt.imshow(img_normal)

    plt.title('Normal image.')

    # Plot 2

    plt.subplot(2, 2, 2)

    plt.plot(hist1, color='b')

    plt.title('Normal image Hist [10-255].')

    # Plot 3

    plt.subplot(2, 2, 3)

    plt.imshow(img_processed)

    plt.title('Cropped image.')

    # Plot 4

    plt.subplot(2, 2, 4)

    plt.plot(hist2, color='b')

    plt.title('Cropped Image Hist [10-255].')

# FIGURE 2

    plt.figure()

    # Plot 1

    plt.subplot(2, 3, 1)

    plt.plot(hist3, color='b')

    plt.title('Normal Image full hist.')

    # Plot 2

    plt.subplot(2, 3, 2)

    plt.plot(hist4, color='b')

    plt.title('Processed Image full hist.')

    # Plot 3

    plt.subplot(2, 3, 3)

    plt.plot(hist3-hist4, color='b')

    plt.title('Difference of Histogramms Norm-Crop.')

    # Plot 4

    plt.subplot(2, 3, 4)

    plt.plot(hist1, color='b')

    plt.title('Normal Image [10-255] Hist.')

    # Plot 5

    plt.subplot(2, 3, 5)

    plt.plot(hist2, color='b')

    plt.title('Cropped Image [10-255] Hist.')

    # Plot

    plt.subplot(2, 3, 6)

    plt.plot(hist1-hist2, color='b')

    plt.title('Difference of Histogramms Norm-Crop [10-255].')

    plt.show()


def crop_a_normal_mammogramm(image_path):
    """This function is using the function of NYU to crop the mammogramm using morphological transformations.
       Takes as inputh the path of a normal mammogramm and returns a plot of histrogramm of its processed and normal version.

    Args:
        image_path (str):
    """
    input_dir = image_path
    output_dir = input_dir.replace('.jpg', "_NYU.jpg")

    cropping_info = crop_mammogram_one_image(
        scan, input_dir, output_dir, 100, 50)

    print(cropping_info)
    import_and_plot_histogramm(input_dir, output_dir)


def majority_filter(image_path, comparison=None):
    """Uses the mahotas computer vision library to implement a majority filter.

    Args:
        image_path (str):  image path should be a full mammogramm.
        comparison (Optional[true,false]): Boolean variable to crop the mammogram and plot a 2x2 of both
            version having processed with the majority filter.
    """
    if comparison is None:

        # loading image
        img = mahotas.imread(image_path)

        # applying majority filter
        new_img = mahotas.majority_filter(img)
        plt.figure()

        # Plot 1

        plt.subplot(2, 2, 1)

        plt.imshow(img)

        plt.title('Normal photo.')

        # Plot 2

        plt.subplot(2, 2, 2)

        plt.imshow(new_img)

        plt.title('Majority Filter.')

        plt.show()

    else:

        output_dir = image_path.replace('.jpg', ".png")

        crop_mammogram_one_image(scan, image_path, output_dir, 100, 50)

        # loading images
        img = mahotas.imread(image_path)
        img_p = mahotas.imread(output_dir)

        # applying majority filter
        new_img = mahotas.majority_filter(img)
        new_img_p = mahotas.majority_filter(img_p)

        plt.figure()

        # Plot 1

        plt.subplot(2, 2, 1)

        plt.imshow(img)

        plt.title('Normal photo.')

        # Plot 2

        plt.subplot(2, 2, 2)

        plt.imshow(new_img)

        plt.title('Majority Filter.')

        # Plot 3

        plt.subplot(2, 2, 3)

        plt.imshow(img_p)

        plt.title('Cropped Photo.')

        # Plot 4

        plt.subplot(2, 2, 4)

        plt.imshow(new_img_p)

        plt.title('Majority Filter.')

        plt.show()


if __name__ == '__main__':

    # Given an image. I croppes it. I saves it. I plots it. It loves it.

    crop_a_normal_mammogramm(
        r'C:\Users\junio\Desktop\Thesis\CBIS_DDSM_Image_Processing\vindr.jpg')

    # run for any path you want as long as it is a full mammogramm.

    majority_filter(
        r'C:\Users\junio\Desktop\Thesis\CBIS_DDSM_Image_Processing\VINDR_MAMMOGRAM.png', True)
