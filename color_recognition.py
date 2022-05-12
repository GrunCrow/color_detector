import pandas as pd
import cv2


# teach the colours -> take csv file from github and load, add the columns name
# (https://github.com/codebrainz/color-names/blob/master/output/colors.csv)
index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

# global variables
clicked = False
r = g = b = x_pos = y_pos = 0
played = True
color_rec = 'Black'

# default image
img = cv2.imread("color_image.jpg")


def recognize_color(red, green, blue):
    minimum = 10000
    c_name = "none"
    for i in range(len(csv)):
        d = abs(red - int(csv.loc[i, "R"])) + abs(green - int(csv.loc[i, "G"])) + abs(blue - int(csv.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            c_name = csv.loc[i, "color_name"]
    return c_name


def load_img(image):
    img = image


# mouse click function
def double_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, x_pos, y_pos, clicked
        clicked = True
        x_pos = x
        y_pos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)

def single_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global b, g, r, x_pos, y_pos, clicked
        clicked = True
        x_pos = x
        y_pos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)


# function for detecting left mouse click
def click(event, x, y, flags, param):
    global clicked, b, g, r, x_pos, y_pos
    if event == cv2.EVENT_LBUTTONDOWN:
        x_pos = x
        y_pos = y
        clicked = True
