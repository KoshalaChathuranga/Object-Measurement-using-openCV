"""
# In the `main` function, a webcam reader instance is created with specific settings 
# for device index, resolution, and frame rate. The program enters a loop to continuously 
# capture frames from the webcam. Each frame is displayed, and a function `draw_bounding_box` 
# is called to identify objects, draw bounding boxes around them, and provide width and height information. 
# The loop terminates when the 'q' key is pressed. Finally, the webcam is released, and windows are closed.

# The `draw_bounding_box` function takes a frame as input, converts it to grayscale, applies thresholding, 
# and identifies contours. Bounding boxes are drawn around objects, and text indicating the width and height 
# of each object is displayed on the frame. The resulting frame is then shown in a separate window.
# """


import cv2
from Read_frames import ReadFrame 

def main():
    webcam_reader = ReadFrame(device_index=0, resolution=(640, 480), frame_rate=30)

    while True:
        frame = webcam_reader.read_frame()
        cv2.imshow("Webcam Frame", frame)
        draw_bounding_box(frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    webcam_reader.release()
    cv2.destroyAllWindows()

def draw_bounding_box(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        text_w = f'Width: {int(w)} pixels'
        text_h = f'Height: {int(h)} pixels'
        
        cv2.putText(frame, text_w, (x + w // 2 - 50, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        cv2.putText(frame, text_h, (x + w + 10, y + h // 2), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

    cv2.imshow('Object', frame)

if __name__ == "__main__":
    main()
