import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


def pencil_sketch(img,blur_kernel = 21,method = 0):
    if img is None:
        print("image array cant be None")
        return None,None
    if blur_kernel < 1 or blur_kernel % 2 == 0 or type(blur_kernel) != int:
        print("Blur kernel must be an odd integer")
        return None,None
    else:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        invt_gray = 255 - gray
        blur = cv2.GaussianBlur(invt_gray, (blur_kernel, blur_kernel), 0)
        invt_blur = 255 - blur

        gray_f = gray.astype(np.float32)
        inv_f = invt_blur.astype(np.float32)

        sketch = np.minimum(255,(gray_f / (inv_f + 1e-6)) * 256)
        sketch = sketch.astype(np.uint8)

        if method == 0:
            return img,sketch

        elif method == 1:
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            h, s, v = cv2.split(hsv)
            v_new = sketch
            s = (s * 0.8).astype(np.uint8)
            colored_hsv = cv2.merge([h, s, v_new])
            colored_sketch = cv2.cvtColor(colored_hsv, cv2.COLOR_HSV2BGR)
            return img,colored_sketch

        elif method != 0 and method != 1:
            print("Method must be 0 or 1")
            return None,None


def display_result(original,sketch, save_path = None):
    original_rgb = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)

    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    axes[0].imshow(original_rgb)
    axes[0].set_title("Original Image")
    axes[0].axis("off")

    axes[1].imshow(sketch, cmap="gray")
    axes[1].set_title("Sketch")
    axes[1].axis("off")

    plt.tight_layout()
    plt.show()

    if save_path is not None:
        save_path = Path(save_path)
        if save_path.suffix == "":
            raise ValueError("save_path must include an extension")
        save_path.parent.mkdir(parents=True, exist_ok=True)
        cv2.imwrite(str(save_path), sketch)



def main():
    bwk = input("Enter the path of the image : ")
    path = bwk.strip(" ")

    if path == "":
        print("Path cant be empty")
        return

    if os.path.exists(path):
        img = cv2.imread(path)
        if img is None:
            print("image is not readable")
            return
        kernel_size = int(input("Enter the size of the kernel : "))
        result_tuple = pencil_sketch(img,kernel_size, method = 0)
        if result_tuple[0] is None and result_tuple[1] is None:
            print("file indictaed cant be read")
            return
        display_result(result_tuple[0],result_tuple[1])
        print("done-displaying")
        return
    else:
        print("Path doesn't exist")
        return


if __name__ == "__main__":
    main()


