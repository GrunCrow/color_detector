import cv2
import os
from gtts import gTTS
from playsound import playsound
import color_recognition as cr


def sound():
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
        text = cr.color_rec + ' R=' + str(cr.r) + ' G=' + str(cr.g) + ' B=' + str(cr.b)
        
        # cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        cv2.putText(frame, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
        
        # For very light colours we will display text in black colour
        if cr.r + cr.g + cr.b >= 600:
            cv2.putText(frame, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

        cv2.imshow("Color Recognition App", frame)

        if cr.played is False:
            cr.played = True
            playsound('{}.mp3'.format(cr.color_rec))
        
        if cr.clicked is True:
            cr.clicked = False
            cr.played = False
            if os.path.exists('{}.mp3'.format(cr.color_rec)):
                os.remove('{}.mp3'.format(cr.color_rec))

            img_name = "frame.jpg"
            cv2.imwrite(img_name, frame)

            img = cv2.imread(img_name)
            cr.load_img(img)
            b, g, r = img[cr.y_pos, cr.x_pos]
            cr.b = int(b)
            cr.g = int(g)
            cr.r = int(r)

            cr.color_rec = cr.recognize_color(r, g, b)
            file_name = cr.color_rec + '.mp3'
            var = gTTS(cr.color_rec, lang='en')
            var.save(file_name)

        # Break the loop when user hits 'q' key
        elif stream & 0xFF == 27:  
            os.remove("frame.jpg")
            os.remove('{}.mp3'.format(cr.color_rec))
            break

    cv2.destroyAllWindows()