import cv2
import os
import color_recognition as cr


# event handler
cv2.namedWindow("Color Recognition App") 
cv2.setMouseCallback("Color Recognition App", cr.click)

cap = cv2.VideoCapture(0) 

while True:
    # Load video every 1ms and to detect user entered key
    stream = cv2.waitKey(1)

    # Read from videoCapture stream and display
    ret, frame = cap.read()
    
    frame = cv2.resize(frame, (0,0), fx=0.99, fy=0.99)  # this fx,fy value will be explained in post
    
    # cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle
    cv2.rectangle(frame, (20, 20), (750, 60), (cr.b, cr.g, cr.r), -1)
    
    # Creating text string to display( Color name and RGB values )
    text = cr.recognize_color(cr.r, cr.g, cr.b) + ' R=' + str(cr.r) + ' G=' + str(cr.g) + ' B=' + str(cr.b)
    
    # cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
    cv2.putText(frame, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
    
    # For very light colours we will display text in black colour
    if cr.r + cr.g + cr.b >= 600:
        cv2.putText(frame, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow("Color Recognition App", frame)

    if cr.clicked is True:
        cr.clicked = False

        img_name = "frame.jpg"
        cv2.imwrite(img_name, frame)

        img = cv2.imread(img_name)
        cr.load_img(img)
        b, g, r = img[cr.y_pos, cr.x_pos]
        cr.b = int(b)
        cr.g = int(g)
        cr.r = int(r)

        os.remove("frame.jpg")

    # Break the loop when user hits 'q' key
    elif stream & 0XFF == ord('q'):  
        break

cv2.destroyAllWindows()