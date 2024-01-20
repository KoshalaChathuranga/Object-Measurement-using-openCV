import cv2

class ReadFrame:
    def __init__(self, device_index=0, resolution=(640, 480), frame_rate=30):
        self.video_capture = cv2.VideoCapture(device_index)

        # Set resolution
        self.video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, resolution[0])
        self.video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, resolution[1])

        # Set frame rate
        self.video_capture.set(cv2.CAP_PROP_FPS, frame_rate)

        # Check if the webcam is opened successfully
        if not self.video_capture.isOpened():
            raise Exception("Error: Could not open webcam.")

    def read_frame(self):
        # Read a frame from the webcam
        ret, frame = self.video_capture.read()

        if not ret:
            raise Exception("Error: Could not read frame from webcam.")

        return frame

    def release(self):
        # Release the webcam when done
        self.video_capture.release()

