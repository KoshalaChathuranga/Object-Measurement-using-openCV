"""
Object Detection and Annotation (draw_custom_rectangle function):

The function converts the current frame to grayscale and applies thresholding to create a binary image (thresh), highlighting potential objects.
Using cv2.findContours, it identifies contours in the binary image.
For each contour found, the code calculates the minimum bounding rectangle (rect) using cv2.minAreaRect. 
The rectangle is specified by its center, dimensions, and rotation angle.
The four corners of the minimum bounding rectangle are obtained using cv2.boxPoints(rect) and converted to integers using np.int0(box).

Instead of directly using the width and height from rect[1], 
    the code calculates the width (w) as the Euclidean distance between the top-left and top-right corners, 
    and the height (h) as the Euclidean distance between the top-right and bottom-right corners using np.linalg.norm.

"""

import cv2
import numpy as np
from Read_frames import ReadFrame

def main():
    webcam_reader = ReadFrame(device_index=0, resolution=(640, 480), frame_rate=30)

    while True:
        frame = webcam_reader.read_frame()
        cv2.imshow("Webcam Frame", frame)
        draw_custom_rectangle(frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    webcam_reader.release()
    cv2.destroyAllWindows()

def draw_custom_rectangle(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Find the minimum area rectangle
        rect = cv2.minAreaRect(contour)
        box = cv2.boxPoints(rect)
        box = np.int0(box)

        # Draw the minimum rectangle
        cv2.drawContours(frame, [box], 0, (0, 255, 0), 2)

        # Calculate width and height based on distances between corners
        w = np.linalg.norm(box[1] - box[0])  # distance between top-left and top-right corners
        h = np.linalg.norm(box[2] - box[1])  # distance between top-right and bottom-right corners

        text_w = f'Width: {int(w)} pixels'
        text_h = f'Height: {int(h)} pixels'
        
        cv2.putText(frame, text_w, (box[1][0], box[1][1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        cv2.putText(frame, text_h, (box[2][0] + 10, box[2][1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

    cv2.imshow('Object', frame)

if __name__ == "__main__":
    main()
