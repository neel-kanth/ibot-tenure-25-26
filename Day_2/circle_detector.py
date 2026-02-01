import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def preprocces_image(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)

    return gray

def detect_circles(gray_image, dp = 1, minDist = 50, param1 = 15, param2 = 30, minRadius = 10, maxRadius = 250):
    circles = cv2.HoughCircles(
    gray_image,
    cv2.HOUGH_GRADIENT,
    dp=dp,
    minDist=minDist,
    param1=param1,
    param2=param2,
    minRadius=minRadius,
    maxRadius=maxRadius
    )
        
    if circles is None:
        return None
    else:
        return circles

def visualize_circles_stats(image , circles , stats , save_path = None):
    if circles is not None:
        size_map = image.copy()
        small_count = 0
        medium_count = 0
        large_count = 0

        circles = np.uint16(np.around(circles))
        for circle in circles[0, :]:
            cx, cy, radius = circle

            if radius < 40:
                color = (0, 0, 255)      
                small_count += 1
            elif radius < 80:
                color = (0, 255, 0)      
                medium_count += 1
            else:
                color = (255, 0, 0)     
                large_count += 1

            cv2.circle(size_map,(cx,cy),radius,color,-1)
            cv2.circle(image, (cx, cy), radius, (0, 255, 0), 2)  # circles
            cv2.circle(image, (cx, cy), 2, (0, 0, 255), 1)  # centre points
            cv2.putText(image, f"Radius:{radius}", (cx, cy - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        stats_text = (
        f"Circles: {stats["number_of_circles"]}\n"
        f"Avg radius: {stats["Avg.Radius"]:.2f}\n"
        f"Min radius: {stats["minRadius"]}\n"
        f"Max radius: {stats["maxRadius"]}"
        )

        fig, axes = plt.subplots(1, 2, figsize=(16, 8))

        axes[0].imshow(image_rgb)
        axes[0].set_title("Highlighted Circles")
        axes[0].axis("off")

        axes[1].imshow(size_map)
        axes[1].set_title("Size Classification Map")
        axes[1].axis("off")

        # Put stats on the right image
        axes[1].text(
            10, 30, stats_text,
            color="yellow",
            fontsize=12,
            bbox=dict(facecolor="black", alpha=0.6)
        )

    plt.tight_layout()

    if save_path is not None:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, bbox_inches="tight", dpi=300)

    plt.show()

def calculate_statistics(circles):
    if circles is None:
        stats = {"number_of_circles" : 0 , "Avg.Radius" : 0 , "minRadius" : 0, "maxRadius" : 0}
        return stats
    else:
        radius_array = [circle[2] for circle in circles[0]]
        stats = {"number_of_circles" : len(radius_array) , "Avg.Radius" : float(np.mean(radius_array)) , 
                "minRadius" : int(np.min(radius_array)), "maxRadius" : int(np.max(radius_array))}
        return stats
        
    
def main():
    path1 = input("enter path to the input : ")
    
    orignal = cv2.imread(path1)
    if orignal is None:
        print("FileNotFound")
        return
    
    image = orignal.copy()

    result = preprocces_image(image)

    circles = detect_circles(result)
    statistics = calculate_statistics(circles)
    
    visualize_circles_stats(image,circles,statistics,save_path="/Users/neelkanthsikdar/Documents/iBot-DC/CV_project/Day_2/cirlce_image_output.jpg",)

    return None
    
    
if __name__ == "__main__":
    main()