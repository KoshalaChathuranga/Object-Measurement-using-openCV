import cv2
import numpy as np
from Read_frames import ReadFrame

pixels_to_mm = 0.1  # Example conversion factor, adjust as needed

def main():
    webcam_reader = ReadFrame(device_index=0, resolution=(640, 480), frame_rate=30)

    while True:
        frame = webcam_reader.read_frame()
        cv2.imshow("Webcam Frame", frame)
        process_frame(frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    webcam_reader.release()
    cv2.destroyAllWindows()

def process_frame(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
                
        num_vertices = len(approx)

        if num_vertices == 4:
            side_lengths = [np.linalg.norm(approx[i] - approx[(i + 1) % 4]) for i in range(4)]
            side_lengths_mm = [length * pixels_to_mm for length in side_lengths]
                     
            # Calculate midpoints of each side
            midpoints = [(approx[i][0] + approx[(i + 1) % 4][0]) // 2 for i in range(4)]
            is_rectangle(side_lengths_mm, *rect_dimensions)

            # Draw the sides and display values at midpoints
            for i in range(4):
                cv2.line(frame, tuple(approx[i][0]), tuple(approx[(i + 1) % 4][0]), (0, 255, 0), 2)
                cv2.putText(frame, f"{side_lengths_mm[i]:.2f} mm", tuple(midpoints[i]), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow('Object', frame)

if __name__ == "__main__":
    main()
