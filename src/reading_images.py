# Copyright (C) 2019 Nan Wu, Jason Phang, Jungkyu Park, Yiqiu Shen, Zhe Huang, Masha Zorin,
#   Stanisław Jastrzębski, Thibault Févry, Joe Katsnelson, Eric Kim, Stacey Wolfson, Ujas Parikh,
#   Sushma Gaddam, Leng Leng Young Lin, Kara Ho, Joshua D. Weinstein, Beatriu Reig, Yiming Gao,
#   Hildegard Toth, Kristine Pysarenko, Alana Lewin, Jiyon Lee, Krystal Airola, Eralda Mema,
#   Stephanie Chung, Esther Hwang, Naziya Samreen, S. Gene Kim, Laura Heacock, Linda Moy,
#   Kyunghyun Cho, Krzysztof J. Geras
#
# This file is part of breast_cancer_classifier.
#
# breast_cancer_classifier is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# breast_cancer_classifier is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with breast_cancer_classifier.  If not, see <http://www.gnu.org/licenses/>.
# ==============================================================================
"""
Defines utility functions for reading png and hdf5 images.
"""
import numpy as np
import imageio.v3 as ii0
import h5py
from PIL import Image


def read_image_png_or_jpeg(file_name):
    """
        For input images that are not in dicom format.
    """
    image = np.array(ii0.imread(file_name))
    # return image
    # return image[:, :, 0]
    return image[:, :]


def read_image_DICOM(file_name):
    """
        For input images that are in dicom format.
    """
    image = np.array(ii0.imread(file_name, plugin='DICOM'))
    # return image
    # return image[:, :, 0]
    return image[:, :]


def read_image_mat(file_name):
    data = h5py.File(file_name, 'r')
    image = np.array(data['image']).T
    data.close()
    return image
