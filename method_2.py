"""
This code employs computer vision techniques to analyze video frames captured from a webcam. 
Its primary goal is to identify objects within the frames and outline them using the minimum bounding rectangle.
The process starts by converting the color image to grayscale, 
            followed by applying a binary threshold to extract object contours. 
The cv2.minAreaRect() function is then utilized to find the minimum area rectangle for each contour. 
The code subsequently draws this rectangle onto the original frame, 
            extracts the width and height from the rotated rectangle, 
            and displays these dimensions alongside the object in real-time. 
The continuous execution of this process enables dynamic object tracking through the webcam feed.
"""
import cv2
import numpy as np
from Read_frames import ReadFrame

def main():
    webcam_reader = ReadFrame(device_index=0, resolution=(640, 480), frame_rate=30)

    while True:
        frame = webcam_reader.read_frame()
        cv2.imshow("Webcam Frame", frame)
        draw_minimum_rectangle(frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    webcam_reader.release()
    cv2.destroyAllWindows()

def draw_minimum_rectangle(frame):
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

        # Extract width and height from the rotated rectangle
        w, h = rect[1]

        text_w = f'Width: {int(w)} pixels'
        text_h = f'Height: {int(h)} pixels'
        
        cv2.putText(frame, text_w, (box[1][0], box[1][1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        cv2.putText(frame, text_h, (box[2][0] + 10, box[2][1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

    cv2.imshow('Object', frame)

if __name__ == "__main__":
    main()
