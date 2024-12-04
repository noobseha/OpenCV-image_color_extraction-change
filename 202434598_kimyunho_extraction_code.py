import cv2
import numpy as np
import matplotlib.pyplot as plt

def show_image(image, title="Image"):
    plt.figure(figsize=(8, 6))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

def extract_regions(image, cloth_lower, cloth_upper, bg_lower, bg_upper):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    cloth_mask = cv2.inRange(hsv, cloth_lower, cloth_upper)
    cloth_region = cv2.bitwise_and(image, image, mask=cloth_mask)

    bg_mask = cv2.inRange(hsv, bg_lower, bg_upper)
    bg_region = cv2.bitwise_and(image, image, mask=bg_mask)

    return cloth_region, bg_region

def main():
    image_path = "lag.jpg" 
    image = cv2.imread(image_path)

    if image is None:
        print("이미지를 불러오지 못했습니다. 경로를 확인하세요.")
        return

    cloth_lower = np.array([90, 50, 50])  
    cloth_upper = np.array([130, 255, 255])  
    bg_lower = np.array([20, 50, 50])  
    bg_upper = np.array([40, 255, 255])  

    cloth_region, bg_region = extract_regions(image, cloth_lower, cloth_upper, bg_lower, bg_upper)

    show_image(cloth_region, "Extracted Cloth Region")
    show_image(bg_region, "Extracted Background Region")

if __name__ == "__main__":
    main()
