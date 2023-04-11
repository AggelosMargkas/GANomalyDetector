import matplotlib.pyplot as plt  # importing matplotlib

# reads image data
img_normal = plt.imread(
    r'C:\Users\junio\Desktop\Thesis\CBIS_DDSM_Image_Processing\manifest-1667995631662\CBIS-DDSM\Calc-Test_P_00077_LEFT_CC\anotherimage.png')

# plt.imshow(img, cmap='gray')
# plt.show()

img_cropped = plt.imread(
    r"C:\Users\junio\Desktop\Thesis\CBIS_DDSM_Image_Processing\outputImages\cropped_image2.png")


histogramm_of__normal = plt.hist(img_normal.ravel(), bins=256, range=(0.0, 1.0),
                                 fc='k', ec='k')  # calculating histogram

histogramm_of__cropped = plt.hist(img_cropped.ravel(), bins=256, range=(0.0, 1.0),
                                  fc='k', ec='k')  # calculating histogram
# plt.show()


fig = plt.figure()


# This represents a (3x1) grid (row x col) and we are plotting the (1) subplot. The last number increments row-wise.
ax = fig.add_subplot(211)

plt.hist(img_normal.ravel(), bins=256, range=(0.0, 1.0),
         fc='k', ec='k')  # calculating histogram

# This represents a (3x2) grid (row x col) and we are plotting the (1) subplot. The last number increments row-wise.
ax = fig.add_subplot(212)

histogramm_of__cropped = plt.hist(img_cropped.ravel(), bins=256, range=(0.0, 1.0),
                                  fc='k', ec='k')  # calculating histogram


plt.show()
