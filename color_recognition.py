import numpy as np
import pandas as pd
import cv2

# define image
# todo create loop to load more images (?)
img = cv2.imread("color_image.jpg")

# teach the colours -> take csv file from github and load, add the columns name
# (https://github.com/codebrainz/color-names/blob/master/output/colors.csv)
index =["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

# global variables
clicked = False
r = g = b = x_pos = y_pos = 0


# todo color recognition function
def recognize_color(R , G, B):
    minimum = 10000
    c_name = "none"
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            c_name = csv.loc[i, "color_name"]
    return c_name


# mouse click function
def mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, x_pos, y_pos, clicked
        clicked = True
        x_pos = x
        y_pos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)

# todo application window
# todo Image version
# todo Add Audio
# todo Video Version
# todo Final Version
