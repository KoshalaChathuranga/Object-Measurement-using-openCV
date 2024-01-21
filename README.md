# Object-Measurement-using-openCV

## Overview

This code provides a simple Python class, 'ReadFrame', for capturing video frames from a webcam using the OpenCV library ('cv2'). The class is designed to initialize the webcam, set its resolution and frame rate, read frames, and release the webcam when done.
Then inside other method file there are 4 different methods to claculate width and height of an object. 

## Method one (method_1.py)

After converting the frame to grayscale and applying binary thresholding, contours are found using cv2.findContours. For each contour, the bounding rectangle is obtained using cv2.boundingRect, providing the coordinates of the top-left corner (x, y) and the width (w) and height (h). 
A green rectangle is drawn around each object, and the frame is annotated with the calculated width and height, providing visual representation and dimensional information for the detected objects.

## Method two (method_2.py)

the width (w) and height (h) of each detected object are calculated based on the minimum area rectangle encompassing the object's contour. 
The minimum area rectangle is determined using cv2.minAreaRect, and the width and height are extracted from the resulting rectangle object (rect). 
These dimensions are then used to annotate the frame with text displaying the width above the second corner and the height to the right of the third corner of the minimum area rectangle.

## Method three (method_3.py)

Here the width (w) and height (h) of each detected object are calculated based on the distances between specific corners of the minimum area rectangle enclosing the object's contour. 
After finding the minimum area rectangle using cv2.minAreaRect, the code extracts the rectangle's four corners (box) and converts them to integer coordinates. Subsequently, the Euclidean distances between specific corners are computed using np.linalg.norm. 
The width is calculated as the distance between the top-left and top-right corners, and the height is calculated as the distance between the top-right and bottom-right corners. 
These width and height values are then used for annotating the frame with text displaying the dimensions of the detected objects.

## Method four (method_4.py)

The process_frame function takes an input frame and performs the following steps:
    
    Contour Identification:
    - Converts the frame to grayscale.
    - Applies binary thresholding to create a binary image (thresh).
    - Identifies contours in the binary image using cv2.findContours.

    Quadrilateral Detection:
    - For each contour, applies the epsilon approximation method using cv2.approxPolyDP 
      to reduce the number of vertices in the contour.
    - If the approximated polygon has four vertices (indicating a quadrilateral), 
      further processing is performed.

    Side Length Calculation:
    - Calculates the side lengths of the quadrilateral using np.linalg.norm 
      by measuring the Euclidean distance between consecutive vertices 
      of the approximated polygon.

    Conversion to Millimeters:
    - Converts the calculated side lengths to millimeters based on a predefined 
      conversion factor (pixels_to_mm).

    Midpoints and Annotation:
    - Calculates the midpoints of each side.
    - Checks if the detected shape is a rectangle using the is_rectangle function.
    - Draws the sides of the quadrilateral on the frame.
    - Displays the calculated side lengths in millimeters at the midpoints 
      using cv2.putText.
    
