import cv2
import numpy as np
import os

import circle_detector as CD

def main(video_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray_frame = CD.preprocces_image(frame)
        circles = CD.detect_circles(gray_frame)
    
        if circles is not None:
            circles = np.uint16(np.around(circles))
            for cx, cy, radius in circles[0]:
                cv2.circle(frame, (cx, cy), radius, (0, 255, 0), 2)
                cv2.circle(frame, (cx, cy), 2, (0, 0, 255), 1)

        cv2.imshow("Video Circle Detection", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main("/Users/neelkanthsikdar/Documents/iBot-DC/CV_project/Day_2/video_circle.mov")



