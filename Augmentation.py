import os
import cv2
import numpy as np

def geometric_augmentation(image):
    scalex = 1.0
    scaley = 1.0
    shearx = 0.0
    sheary = 0.0
    shiftx = 0.0
    shifty = 0.0

    rand_val = np.random.random()
    if rand_val < 0.3:
        scalex = np.random.uniform(0.7, 1.5)
        scaley = np.random.uniform(0.7, 1.5)
    elif rand_val < 0.6:
        shearx = np.random.uniform(-0.2, 0.2)
        sheary = np.random.uniform(-0.2, 0.2)
    else:
        shiftx = int(np.random.uniform(-0.1, 0.1) * image.shape[1])
        shifty = int(np.random.uniform(-0.1, 0.1) * image.shape[0])
    transformation_matrix = np.float32([
        [scalex, shearx, shiftx],
        [sheary, scaley, shifty]
    ])
    result = cv2.warpAffine(image, transformation_matrix, (image.shape[1], image.shape[0]))
    return result
def color_augmentation(image):
    rand_val = np.random.random()
    if rand_val < 0.5:
        brightness_factor = 30
        result = np.clip(image.astype(np.int16) + brightness_factor, 0, 255).astype(np.uint8)
    elif rand_val <1:
        contrast = np.random.uniform(0.6, 1.4)
        result = np.clip(image.astype(np.float32) * contrast, 0, 255).astype(np.uint8)
    return result
def random_noise(image):
    noise = np.random.normal(0,15,image.shape)
    result = np.clip(image.astype(np.float32)+noise , 0, 255).astype(np.uint8)
    return result
def rotation(image):
    angle = np.random.uniform(-20, 20)
    center = (image.shape[0] // 2, image.shape[1] // 2)
    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    result = cv2.warpAffine(image, matrix, (image.shape[0], image.shape[1]))
    return result
def hue_shift(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV).astype(np.float32)
    del_hue = np.random.randint(-30, 30)

    hue_values = hsv[::, ::, 0]

    hsv[:, :, 0] = (hsv[:, :, 0] + del_hue) % 180
    result = cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2BGR)

    return result
def augmentation(image,x):
    if x == 0:
        result = geometric_augmentation(image)
        return result
    elif x == 1:
        result = color_augmentation(image)
        return result
    elif x == 2:
        result = random_noise(image)
        return result
    elif x == 3:
        result = rotation(image)
        return result
    elif x == 4:
        result = hue_shift(image)
        return result
    else:
        return None


path_to_folder_read = "/Users/neelkanthsikdar/Downloads/sample_images"
output_folder = "/Users/neelkanthsikdar/Downloads/output_folder"

def main(path_to_folder_read,path_to_output_folder):
    for file in os.listdir(path_to_folder_read):
        path_to_file = os.path.join(path_to_folder_read, file)
        img = cv2.imread(path_to_file)
        if img is not None:
            print(f"proccesing: {file}")
            base_name = os.path.basename(file)
            name_only, extension = os.path.splitext(file)
            for i in range(5):
                augmented = augmentation(img,i)
                if augmented is not None:
                    augmented_imgname = f"{name_only}_aug_{i}{extension}"
                    path_to_write = os.path.join(path_to_output_folder, augmented_imgname)
                    cv2.imwrite(path_to_write, augmented)
        else:
            print(f"Error reading the file : {file} , path = {path_to_file}")
            continue

    print(f"done writing to {output_folder}")
    print(os.listdir(output_folder))
    return

if __name__ == "__main__":
    path_to_folder_read = eval(input("Enter the folder to read path : "))
    path_to_output_folder = eval(input("Enter the output folder : "))

    if not os.path.exists(path_to_output_folder):
        print(f"The output folder {path_to_output_folder} does not exist")
    else:
        main(path_to_folder_read,output_folder)