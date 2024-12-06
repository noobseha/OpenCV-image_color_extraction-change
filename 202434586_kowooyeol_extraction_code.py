import cv2
import numpy as np
import matplotlib.pyplot as plt


def show_image(image, title="Image"):
    plt.figure(figsize=(8, 6))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()


def extract_regions(image, bg_lower, bg_upper):
    
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    bg_mask = cv2.inRange(hsv, bg_lower, bg_upper)
    bg_region = cv2.bitwise_and(image, image, mask=bg_mask)

    return bg_region  


def main():
    # 이미지 파일 경로
    image_path = "202434586_Kowooyeol_original.png"  
    image = cv2.imread(image_path)

    if image is None:
        print("이미지를 불러오지 못했습니다. 경로를 확인하세요.")
        return

    # 노란색 배경을 위한 색상 범위 설정 (HSV 값)
    bg_lower = np.array([20, 100, 100])  # 배경 색상 하한값 (노란색 하한)
    bg_upper = np.array([40, 255, 255])  # 배경 색상 상한값 (노란색 상한)

    bg_region = extract_regions(image, bg_lower, bg_upper)

    show_image(bg_region, "Extracted Background Region")

if __name__ == "__main__":
    main()
