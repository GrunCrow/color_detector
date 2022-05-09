import numpy as np
import pandas as pd
import cv2
import os

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


#function for detecting left mouse click
def click(event, x,y, flags, param):
    global clicked, b, g, r, x_pos, y_pos
    if event == cv2.EVENT_LBUTTONDOWN:
        x_pos = x
        y_pos = y
        clicked = True

         
#event handler
cv2.namedWindow("Color Recognition App") 
cv2.setMouseCallback("Color Recognition App", click)
     

cap = cv2.VideoCapture(0) 

while (True):

    #Load video every 1ms and to detect user entered key
    stream = cv2.waitKey(1)   
     
    #Read from videoCapture stream and display
    ret,frame = cap.read()
    
    frame = cv2.resize(frame, (0,0), fx=0.99, fy=0.99)  #this fx,fy value will be explained in post
    
    # cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle
    cv2.rectangle(frame, (20, 20), (750, 60), (b, g, r), -1)
    
    # Creating text string to display( Color name and RGB values )
    text = recognize_color(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
    
    # cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
    cv2.putText(frame, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
    
    # For very light colours we will display text in black colour
    if r + g + b >= 600:
        cv2.putText(frame, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow("Color Recognition App", frame)

    
    if clicked is True:
        clicked = False

        img_name = "frame.jpg"
        cv2.imwrite(img_name, frame)

        img = cv2.imread(img_name)
        b, g, r = img[y_pos, x_pos]
        b = int(b)
        g = int(g)
        r = int(r)

        os.remove("frame.jpg")

    # Break the loop when user hits 'q' key
    elif stream & 0XFF == ord('q'):  
        break

cv2.destroyAllWindows()