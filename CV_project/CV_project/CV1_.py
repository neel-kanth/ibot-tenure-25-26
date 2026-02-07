import cv2
import numpy as np
import os

import CV1  #the other file


def video_sketch(path,color = False):
    cap = cv2.VideoCapture(path)
    if not cap.isOpened():
        raise IOError("Cannot open video file")
    kernel_size = int(input("Enter the size of the kernel : "))

    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    file_output = input("enter the output file name : ")
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter("output_sketch.mp4", fourcc, fps, (width, height), isColor = color)

    processed = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame, sketch = CV1.pencil_sketch(frame, 11, method = color)

        out.write(sketch)
        processed += 1

        percent = (processed / total_frames) * 100
        print(f"\rProgress: {percent:.2f}%", end="")

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("keyboard interrupt")
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    return


def main():
    bwk = input("Enter the path of the viode file : ")
    path = bwk.strip(" ")
    if path == "":
        print("Path cant be empty")
        return
    if os.path.exists(path):
        video_sketch(path,color = True)
    else:
        print("Path doesn't exist")
        return

if __name__ == "__main__":
    main()