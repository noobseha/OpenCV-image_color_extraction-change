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

   
    cloth_mask_1 = cv2.inRange(hsv, cloth_lower[0], cloth_upper[0])  # 첫 번째 범위
    cloth_mask_2 = cv2.inRange(hsv, cloth_lower[1], cloth_upper[1])  # 두 번째 범위
    cloth_mask = cv2.bitwise_or(cloth_mask_1, cloth_mask_2)  # 두 마스크를 합침
    cloth_region = cv2.bitwise_and(image, image, mask=cloth_mask)

    
    bg_mask = cv2.inRange(hsv, bg_lower, bg_upper)
    bg_region = cv2.bitwise_and(image, image, mask=bg_mask)

    return cloth_region, bg_region


def main():
    
    image_path = "./original.png"  # 이미지 파일 경로를 변경하세요
    image = cv2.imread(image_path)

    if image is None:
        print("이미지를 불러오지 못했습니다. 경로를 확인하세요.")
        return

   
    cloth_lower = [np.array([140, 50, 50]), np.array([170, 50, 50])]  # 핑크색 하한값
    cloth_upper = [np.array([170, 255, 255]), np.array([180, 255, 255])]  # 핑크색 상한값

   
    bg_lower = np.array([0, 0, 0])  # 검정색 하한값 (Saturation과 Value가 낮은 범위)
    bg_upper = np.array([180, 50, 50])  # 검정색 상한값 (Saturation과 Value가 낮은 범위)

   
    cloth_region, bg_region = extract_regions(image, cloth_lower, cloth_upper, bg_lower, bg_upper)

   
    show_image(cloth_region, "Extracted Cloth Region")
    show_image(bg_region, "Extracted Background Region")


if __name__ == "__main__":
    main()
