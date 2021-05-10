# pip install colour-science
import colour
from colour.plotting import *
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

chart = [[115,  82,  68], [194, 150, 130], [ 98, 122, 157], [ 87, 108,  67], [133, 128, 177], [103, 189, 170],
         [214, 126,  44], [ 80,  91, 166], [193,  90,  99], [ 94,  60, 108], [157, 188,  64], [224, 163,  46],
         [ 56,  61, 150], [ 70, 148,  73], [175,  54,  60], [231, 199,  31], [187,  86, 149], [  8, 133, 161],
         [243, 243, 242], [200, 200, 200], [160, 160, 160], [122, 122, 121], [ 85,  85,  85], [ 52,  52,  52]
         ]

# plot_single_colour_checker('ColorChecker 2005')
# plot_chromaticity_diagram_CIE1931()
plot_RGB_colourspaces_in_chromaticity_diagram_CIE1931(['ITU-R BT.709'], plot_kwargs=[{'color': 'gray'}])


for i in range(24):
    print('{} '.format(chart[i]), end='')
    if (i+1) % 6 == 0 and i != 0:
        print('')