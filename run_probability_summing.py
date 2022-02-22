import matplotlib.pyplot as plt

from ProbabilityMapSumming import ProbabilityMapSummer
import pandas as pd

summer = ProbabilityMapSummer()

base_path = "/home/micha/Documents/01_work/git/moma_area_estimation_testing/data/Pos25_GL31/"
csv_input_path = base_path + "ExportedCellStats__20200812_8proms_ace_1_MMStack_Pos25_GL31.tif.csv"
mask_path = base_path + "ExportedCellMasks__20200812_8proms_ace_1_MMStack_Pos25_GL31.tif.tif"
probability_map_path = base_path + "20200812_8proms_ace_1_MMStack_Pos25_GL31__model_9e5727e4ed18802f4ab04c7494ef8992d798f4d64d5fd75e285b9a3d83b13ac9.tif"
csv_output_path = base_path + "ExtendedExportedCellStats__20200812_8proms_ace_1_MMStack_Pos25_GL31.tif.csv"

summer.read(mask_path, probability_map_path, csv_input_path)
summer.calculateProbabilities()
summer.save(csv_output_path)
# plt.scatter(summer.df_out['area_px'], summer.df_out['prob_area__px'])
# plt.show()
#
# plt.scatter(summer.df_out['length_px'], summer.df_out['prob_area__px'])
# plt.show()

print('Finished')
