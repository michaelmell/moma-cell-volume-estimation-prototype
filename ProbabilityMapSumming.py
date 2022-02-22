# from skimage.io import imread
from skimage.morphology import binary_dilation, binary_erosion
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tifffile.tifffile as tff

class ProbabilityMapSummer(object):
    def __init__(self):
        self.masks = None
        self.probs = None
        self.df = None
        self.df_out = None

    def calculateProbabilities(self):
        # self.df.head()
        self.df_out = self.df.copy()
        self.df_out['area_probability_sum__px'] = None
        for index, row in self.df.iterrows():
            mask = self.masks[row.frame, 0, ...] == row.cell_ID
            prob = self.probs[row.frame, ...]
            core, border = self.calculateBorderAndCore(mask)
            # core, border = self.calculateBorderAndCore2(mask)
            # imshow(prob)
            # imshow(border)
            prob_weighted_area = self.sumProbabilities(core, border, prob)
            # row['area_summed_probilities__px'] = prob_weighted_area
            # print(f"area: {row['area_px']}, {row['area_summed_probilities__px']}")
            self.df_out['area_probability_sum__px'][index] = prob_weighted_area

    def sumProbabilities(self, core, border, prob):
        core_sum = np.sum(core)
        border_sum = np.sum(prob[border])
        border_pixels_total = np.sum(border)
        return core_sum + border_sum

    def calculateBorderAndCore(self, mask):
        mask_dilated = binary_dilation(mask)
        core = binary_erosion(mask)
        border = np.logical_and(mask_dilated, ~core)
        return core, border

    def calculateBorderAndCore2(self, mask):
        weight_mask_dilation_se_size = 5  # use '3': to get 1 pixel dilation; use '5': to get 2 pixel dilation
        weight_mask_dilation_se = np.ones((weight_mask_dilation_se_size, weight_mask_dilation_se_size))
        mask_dilated = binary_dilation(mask, weight_mask_dilation_se)  # dilate edge to cover broader region
        core = binary_erosion(mask, weight_mask_dilation_se)  # dilate edge to cover broader region
        border = np.logical_and(mask_dilated, ~core)
        return core, border

    def read(self, mask_path, prob_path, previous_csv_path):
        self.masks = tff.imread(mask_path)
        self.probs = tff.imread(prob_path)
        self.df = pd.read_csv(previous_csv_path, skiprows=4, delimiter=',')
        pass

    def save(self, csv_output_path):
        self.df_out.to_csv(csv_output_path)
        pass


def imshow(imdata):
    plt.imshow(imdata, interpolation='none')
    plt.show()
