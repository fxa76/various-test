# create a color palette based on an initial color

from matplotlib import pyplot as plt
import seaborn as sb

# display a palette
# current_palette = sb.color_palette("mako",15)
# current_palette = sb.cubehelix_palette(start=.5, rot=-.5, dark=0, light=.95, n_colors=15)
# sb.palplot(current_palette)
# plt.show()

import colorsys
#define number of colors
N = 15
#define base color in r,g,b
base_color_hsv = colorsys.rgb_to_hsv(0.0,119/255,212/255)
print("base color HSV {}".format(base_color_hsv))

#init HSV
c = list(base_color_hsv)
# c[1]=1.0
# c[2]=1.0
base_color_hsv= tuple( c )

HSV_tuples = [(base_color_hsv[0] , base_color_hsv[1]-x*1/N , base_color_hsv[2]) for x in range(N)]
RGB_tuples = []
for c in HSV_tuples:
    print(c)
    rgb = map(lambda x: x, colorsys.hsv_to_rgb(*c))
    RGB_tuples.append(list(rgb))

colors =  RGB_tuples
print(colors)


#display the colors
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

cmap = ListedColormap(colors)
a = np.outer(np.linspace(0, 1, N), np.linspace(0, 1, N))
im = plt.imshow(a, cmap=cmap)
plt.colorbar(im)
plt.show()

