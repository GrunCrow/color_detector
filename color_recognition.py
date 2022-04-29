import numpy as np
import pandas as pd
import cv2

# define image
# todo create loop to load more images (?)
img = cv2.imread("color_image.jpg")

# teach the colours -> take csv file from github and load, add the columns name
# (https://github.com/codebrainz/color-names/blob/master/output/colors.csv)
index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

# global variables
clicked = False
r = g = b = x_pos = y_pos = 0


def recognize_color(red, green, blue):
    minimum = 10000
    c_name = "none"
    for i in range(len(csv)):
        d = abs(red - int(csv.loc[i, "R"])) + abs(green - int(csv.loc[i, "G"])) + abs(blue - int(csv.loc[i, "B"]))
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


cv2.namedWindow('Color Recognition App')
cv2.setMouseCallback('Color Recognition App', mouse_click)

while 1:
    cv2.imshow("Color Recognition App", img)

    if clicked:
        # cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle
        cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)
        # Creating text string to display( Color name and RGB values )
        text = recognize_color(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)

        # cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
        # For very light colours we will display text in black colour
        if r + g + b >= 600:
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

        clicked = False

    # Break the loop when user hits 'esc' key
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()

# todo Image version
# todo Add Audio
# todo Video Version
# todo Final Version
