import cv2
import subprocess
import os
from PIL import Image

pathCounter = 108

# define the callback function for mouse events
def mouse_callback(event, x, y, flags, param):
    global pathCounter
    # if left mouse button is clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # if click is on button
        if button_x < x < button_x + button_width and button_y < y < button_y + button_height:
            #print("Button clicked!")
            ret, frame = cap.read()
            cv2.imwrite('frame.jpg', frame)

            #run detect.py on the image from the webcam
            subprocess.run(['python3', 'detect.py', '--weights', 'main.pt', '--conf', '0.25', '--img-size', '640', '--source', 'frame.jpg'], capture_output=True)
            os.remove('frame.jpg')

            # return back the image that detect.py outputted
            pathCounter+=1
            path = r"/Users/AdityaKulkarni/yolov7/runs/detect/{}/frame.jpg".format("exp{}".format(pathCounter))   #path/yolov7/runs/detect/expXX/frame.jpg, with XX being a numbered folder generated from detect.py
            im = Image.open(path)
            im.show()

# access the webcam, 0 for main, 1 for external
cap = cv2.VideoCapture(1)

# make sure webcam successfully opened
if not cap.isOpened():
    print("Could not open webcam")
    exit()

# create our button
button_text = "Click to Process"
button_x = 805
button_y = 1000
button_width = 400
button_height = 45
button_color = (87, 66, 245)
button_text_color = (255, 2555, 255)

# loop through frames of the webcam stream
while True:
    # read a frame
    ret, frame = cap.read()

    # implement our button to the frame
    #cv2.rectangle(frame, (button_x, button_y), (button_x + button_width, button_y + button_height), button_color, -1)
    #cv2.putText(frame, button_text, (button_x + 42, button_y + 35), cv2.FONT_HERSHEY_SIMPLEX, 1.2, button_text_color, 1)

    # display webcam
    cv2.imshow("Webcam", frame)

    # register mouse callback function
    cv2.setMouseCallback("Webcam", mouse_callback)

    # if q is pressed, break
    if cv2.waitKey(1) == ord('q'):
        break

# release webcam and close window
cap.release()
cv2.destroyAllWindows()
