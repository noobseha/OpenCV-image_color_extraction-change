import cv2
import numpy as np
import matplotlib.pyplot as plt

def show_image(image, title="Image"):
    plt.figure(figsize=(8, 6))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

def change_colors(image, cloth_lower, cloth_upper, bg_lower, bg_upper, new_cloth_color, new_bg_color):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    cloth_mask = cv2.inRange(hsv, cloth_lower, cloth_upper)
    image[np.where(cloth_mask != 0)] = new_cloth_color

    bg_mask = cv2.inRange(hsv, bg_lower, bg_upper)
    image[np.where(bg_mask != 0)] = new_bg_color

    return image

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

    new_cloth_color = [0, 255, 255]  
    new_bg_color = [255, 191, 0]  

    modified_image = change_colors(image.copy(), cloth_lower, cloth_upper, bg_lower, bg_upper, new_cloth_color, new_bg_color)

    show_image(modified_image, "Modified Image")

if __name__ == "__main__":
    main()
